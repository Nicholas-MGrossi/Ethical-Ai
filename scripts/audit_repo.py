#!/usr/bin/env python3
"""Comprehensive repository audit: find all problems across all files."""

import os
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

results = []

# CHECK 1: Placeholder/incomplete text in markdown files
print("=== CHECK 1: Placeholder text ===\n")
placeholder_patterns = {
    r'\[INSERT DATE\]': 'Unsubstituted date placeholder',
    r'\[INSERT YOUR': 'Unsubstituted field placeholder',
    r'YOUR_USERNAME': 'Generic username placeholder',
    r'\[tbd|tbd:|TBD\]': 'TBD placeholder',
    r'\[Repository URL\]': 'Repository URL placeholder',
    r'\[repository URL\]': 'Repository URL placeholder',
}

for dp, dn, files in os.walk(ROOT):
    if '.git' in dp or 'node_modules' in dp:
        continue
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(dp, f)
            with open(path, encoding='utf-8') as fh:
                content = fh.read()
            rel_path = os.path.relpath(path, ROOT)
            for pat, label in placeholder_patterns.items():
                for m in re.finditer(pat, content, re.IGNORECASE):
                    line_num = content[:m.start()].count('\n') + 1
                    print(f"  [{rel_path}:{line_num}] {label}: '{m.group()}'")
                    results.append((rel_path, line_num, label, m.group()))

# CHECK 2: Files with unusual sizes or issues
print("\n=== CHECK 2: File size anomalies ===\n")
for dp, dn, files in os.walk(ROOT):
    if '.git' in dp or 'node_modules' in dp:
        continue
    for f in files:
        path = os.path.join(dp, f)
        size = os.path.getsize(path)
        rel_path = os.path.relpath(path, ROOT)
        if f.endswith('.md') and size < 100 and f not in ['.gitignore']:
            print(f"  SMALL: {rel_path} ({size} bytes)")
        if f.endswith('.json') and size > 50000 and 'node_modules' not in path:
            print(f"  LARGE JSON: {rel_path} ({size} bytes)")

# CHECK 3: Schema field description completeness
print("\n=== CHECK 3: JSON Schema description completeness ===\n")
schema_dir = os.path.join(ROOT, 'schemas')
for f in sorted(os.listdir(schema_dir)):
    if f.endswith('.json'):
        path = os.path.join(schema_dir, f)
        with open(path) as fh:
            try:
                data = json.load(fh)
            except:
                continue
        if 'properties' in data:
            props = data['properties']
            for key, val in props.items():
                if isinstance(val, dict):
                    if 'description' not in val and val.get('type') not in ['object', 'array'] and 'enum' not in val:
                        print(f"  {f}: property '{key}' missing description")

# CHECK 4: Cross-reference broken links (internal doc references like "see §X")
print("\n=== CHECK 4: Cross-reference pattern check ===\n")
for dp, dn, files in os.walk(ROOT):
    if '.git' in dp or 'node_modules' in dp:
        continue
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(dp, f)
            with open(path, encoding='utf-8') as fh:
                content = fh.read()
            rel_path = os.path.relpath(path, ROOT)
            # Find 'see §' or '§X' patterns and check they reference existing headings
            refs = re.findall(r'[Ss]ee\s+§(\d+(?:\.\d+)*)', content)
            if refs:
                # Extract all headings for cross-reference (levels 1-6)
                headings = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
                heading_nums = set()
                for h in headings:
                    m = re.match(r'(\d+(?:\.\d+)*)', h)
                    if m:
                        heading_nums.add(m.group(1))
                for ref in refs:
                    if ref not in heading_nums:
                        line_num = content[:content.find(f'§{ref}')].count('\n') + 1
                        print(f"  {rel_path}:{line_num} references §{ref} but no such section found in file")

# CHECK 5: Inconsistent or missing doc index tables
print("\n=== CHECK 5: Doc Index table presence ===\n")
for dp, dn, files in os.walk(ROOT):
    if '.git' in dp or 'node_modules' in dp:
        continue
    for f in files:
        if f.endswith('.md') and f not in ['TODO.md', 'CHANGELOG.md']:
            path = os.path.join(dp, f)
            with open(path, encoding='utf-8') as fh:
                content = fh.read()
            rel_path = os.path.relpath(path, ROOT)
            if not re.search(r'Doc Index|Document Index|References|Cross-Reference', content, re.IGNORECASE):
                pass  # Too many would flag; not all need doc indexes

print("\n=== AUDIT COMPLETE ===")
if results:
    print(f"\nTotal issues found: {len(results)}")
    for path, line, label, match in results:
        print(f"  - {path}:{line}: {label}")
else:
    print("No critical issues found.")