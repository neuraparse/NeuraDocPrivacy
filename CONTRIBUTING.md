# Contributing to NeuraDocPrivacy

Thank you for your interest in contributing to NeuraDocPrivacy! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported. When creating a bug report, include:

- **Clear and descriptive title**
- **Detailed description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Environment information**:
  - Operating system and version
  - Python version
  - Package versions (run `pip freeze`)
- **Screenshots** if applicable
- **Sample PDF file** (if the issue is PDF-specific)

### Suggesting Enhancements

We welcome feature requests! When suggesting enhancements:

- **Clear and descriptive title**
- **Detailed description** of the proposed feature
- **Use case** and why this feature would be useful
- **Mockups or examples** if applicable

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following the coding standards below
4. **Test your changes** thoroughly
5. **Commit your changes** with clear commit messages
6. **Push to your fork** and submit a pull request

## 📋 Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Setup Steps

1. **Clone your fork**:
   ```bash
   git clone https://github.com/neuraparse/NeuraDocPrivacy.git
   cd NeuraDocPrivacy
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]
   ```

4. **Install spaCy model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 🎨 Coding Standards

### Python Code Style

- Follow **PEP 8** style guidelines
- Use **type hints** for function parameters and return values
- Keep functions **small and focused**
- Use **descriptive variable names**
- Add **docstrings** for all public functions and classes

### Code Formatting

We use **Black** for code formatting. Before committing:

```bash
black .
```

### Linting

We use **flake8** for linting. Check your code:

```bash
flake8 .
```

### Type Checking

We use **mypy** for type checking:

```bash
mypy .
```

## 🧪 Testing

### Running Tests

```bash
pytest
```

### Test Coverage

```bash
pytest --cov=.
```

### Writing Tests

- Write tests for new functionality
- Aim for good test coverage
- Use descriptive test names
- Test both success and failure cases

## 📝 Documentation

### Code Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Include type hints
- Provide examples for complex functions

### README Updates

- Update README.md if you add new features
- Include usage examples
- Update installation instructions if needed

## 🔄 Pull Request Process

1. **Ensure your code follows the style guidelines**
2. **Add tests for new functionality**
3. **Update documentation** as needed
4. **Make sure all tests pass**
5. **Update the CHANGELOG.md** with your changes
6. **Submit the pull request**

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## 🏷️ Version Control

### Commit Messages

Use clear, descriptive commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

### Branch Naming

- `feature/feature-name` - New features
- `bugfix/issue-description` - Bug fixes
- `hotfix/critical-fix` - Critical fixes
- `docs/documentation-update` - Documentation updates

## 🚀 Release Process

### Version Numbers

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality
- **PATCH** version for backwards-compatible bug fixes

### Release Checklist

- [ ] All tests pass
- [ ] Documentation is up to date
- [ ] CHANGELOG.md is updated
- [ ] Version number is updated in setup.py
- [ ] Release notes are prepared

## 📞 Getting Help

If you need help with contributing:

1. **Check existing issues** and pull requests
2. **Search the documentation**
3. **Create an issue** with the "question" label
4. **Join our discussions** in GitHub Discussions

## 🙏 Recognition

Contributors will be recognized in:

- The project README
- Release notes
- GitHub contributors page

Thank you for contributing to NeuraDocPrivacy! 🎉 