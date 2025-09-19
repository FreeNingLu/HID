# Contributing to HID Format

Thank you for your interest in contributing to the HID Format project! We welcome contributions that improve the decoder, benchmarks, and documentation.

## 📋 Before You Contribute

### Patent Notice
⚠️ **Important**: The HID encoding algorithm is protected by patent (CN202410xxxxx). The encoder implementation remains proprietary. Contributions should focus on:
- Decoder improvements
- Performance benchmarks
- Documentation
- Examples and tutorials
- Bug fixes

## 🚀 Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/FreeNingLu/HID.git
   cd HID
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Run Tests**
   ```bash
   pytest tests/
   ```

## 📝 Contribution Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use Black for formatting: `black .`
- Run flake8 for linting: `flake8 .`
- Add type hints where applicable

### Testing
- Write tests for new features
- Maintain test coverage above 80%
- Run tests before submitting PR: `pytest --cov`

### Documentation
- Update docstrings for new functions
- Add examples in docstrings
- Update README if needed

## 🔄 Pull Request Process

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clean, documented code
   - Add tests
   - Update documentation

3. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation
   - `test:` Testing
   - `perf:` Performance improvement

4. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🎯 Areas for Contribution

### High Priority
- 🐛 Bug fixes in decoder
- 📊 Additional benchmarks
- 📚 Documentation improvements
- 🌍 Internationalization

### Good First Issues
- Add more example files
- Improve error messages
- Add CLI features
- Write tutorials

### Advanced
- Optimize decoder performance
- Add streaming support
- Implement parallel processing
- Create visualization tools

## 🤝 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive criticism
- Respect the patent and licensing terms

### Unacceptable Behavior
- Harassment or discrimination
- Attempting to reverse-engineer the encoder
- Violating patent terms
- Spam or advertising

## 📬 Communication

- **Issues**: [GitHub Issues](https://github.com/FreeNingLu/HID/issues)
- **Discussions**: [GitHub Discussions](https://github.com/FreeNingLu/HID/discussions)
- **Email**: contribute@hid-format.com

## 🏆 Recognition

Contributors will be:
- Listed in AUTHORS.md
- Mentioned in release notes
- Acknowledged in research papers (for significant contributions)

## ⚖️ Legal

By contributing, you agree that:
1. Your contributions will be licensed under MIT License
2. You respect the patent protection on the encoding algorithm
3. You have the right to submit your contributions

## 🙏 Thank You!

Your contributions help make HID the standard for AI-native music representation. Every contribution, no matter how small, is valuable and appreciated!