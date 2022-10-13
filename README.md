# merge-lit
This is a tool to merge result of LLVM Integrated Tester (lit).

- [lit](https://llvm.org/docs/CommandGuide/lit.html)
- [test-suite Guide](https://llvm.org/docs/TestSuiteGuide.html)

# Usage
The below command will merge 'foo.json' and 'bar.json' and save it as 'merged.json'.

```
python3 merge-lit.py foo.json bar.json -o merged.json
```

