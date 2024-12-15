
### 2. `retrieve.md`
```markdown
# Retrieve Operation

```python
# Retrieving the created book
book = Book.objects.get(title="1984")
# Expected output: <Book: 1984> (or similar representation)
