# NeuraDocPrivacy GitHub Setup Guide

This guide will help you set up the NeuraDocPrivacy project on GitHub.

## 🚀 Quick Start

### 1. Initialize Git Repository

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: NeuraDocPrivacy PDF masking tool"

# Add remote repository (replace with your GitHub username)
git remote add origin https://github.com/yourusername/NeuraDocPrivacy.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 2. GitHub Repository Setup

1. **Create Repository on GitHub**:
   - Go to https://github.com/new
   - Repository name: `NeuraDocPrivacy`
   - Description: `A sophisticated PDF document privacy masking tool using NLP`
   - Make it Public or Private (your choice)
   - Don't initialize with README (we already have one)

2. **Set up Repository Settings**:
   - Go to Settings → Pages
   - Enable GitHub Pages (optional, for documentation)
   - Go to Settings → Branches
   - Add branch protection rule for `main` branch

3. **Set up Repository Settings**:
   - Go to Settings → Pages (optional, for documentation)
   - Go to Settings → Branches
   - Add branch protection rule for `main` branch

### 3. Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install spaCy model
python -m spacy download en_core_web_sm

# Install development dependencies (optional)
pip install -e ".[dev]"
pre-commit install
```

### 4. Development Workflow

```bash
# Run tests
make test

# Run linting
make lint

# Format code
make format

# Run the application
make run
```

## 📋 Repository Structure

```
NeuraDocPrivacy/
├── .github/                 # GitHub Actions workflows
├── tests/                   # Test files
├── main.py                  # Main GUI application
├── pdf_masker.py           # Core masking functionality
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── pyproject.toml         # Modern Python project config
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
├── .gitignore             # Git ignore rules
├── .pre-commit-config.yaml # Code quality hooks
├── Makefile               # Development tasks
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Multi-container setup
└── main.spec              # PyInstaller specification
```

## 🔧 Configuration Files

### Git Configuration
- `.gitignore`: Excludes build artifacts, virtual environments, and sensitive files
- `.pre-commit-config.yaml`: Ensures code quality on commits

### Python Configuration
- `pyproject.toml`: Modern Python project configuration
- `setup.py`: Package installation and distribution
- `requirements.txt`: Production dependencies

### Development Tools
- `Makefile`: Common development tasks
- `Dockerfile`: Containerization
- `docker-compose.yml`: Multi-service development environment

## 🚀 Deployment Options

### 1. Local Installation
```bash
pip install -e .
neura-doc-privacy  # Run GUI
pdf-masker --help  # Run CLI
```

### 2. Docker Deployment
```bash
# Build and run with Docker
docker build -t neura-doc-privacy .
docker run -it --rm -v $(pwd)/pdfs:/app/pdfs neura-doc-privacy

# Or use docker-compose
docker-compose up neura-doc-privacy
```

### 3. PyInstaller Executable
```bash
# Build standalone executable
pyinstaller main.spec
# Executable will be in dist/ directory
```

## 📊 Development Workflow

For local development:

1. **Testing**: Run `make test` or `pytest tests/`
2. **Linting**: Run `make lint` or `flake8 .`
3. **Type Checking**: Run `mypy . --ignore-missing-imports`
4. **Coverage**: Run `pytest tests/ --cov=. --cov-report=html`
5. **Building**: Run `pyinstaller main.spec` for executables
6. **Formatting**: Run `make format` or `black .`

## 🔐 Security Considerations

1. **No Sensitive Data**: The `.gitignore` excludes sensitive files
2. **Local Processing**: All PDF processing happens locally
3. **No Data Transmission**: No data is sent to external servers
4. **Container Security**: Docker setup uses non-root user

## 📈 Project Management

- **Issues**: GitHub Issues for bug tracking
- **Discussions**: GitHub Discussions for community engagement
- **Releases**: Manual releases via git tags
- **Documentation**: Keep README and CHANGELOG updated

## 🎯 Next Steps

1. **Update Repository URLs**: Replace `yourusername` in all files with your actual GitHub username
2. **Create Issues**: Add initial issues for planned features
3. **Set up Wiki**: Create project wiki for detailed documentation
4. **Set up Branch Protection**: Protect main branch from direct pushes
5. **Create Release Tags**: Use semantic versioning for releases

## 🔄 Maintenance

### Regular Tasks
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Run tests: `make test`
- Update documentation: Keep README and CHANGELOG current
- Review security: Check for vulnerabilities in dependencies

### Release Process
1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create and push tag: `git tag v1.2.1 && git push origin v1.2.1`
4. Build and test locally: `make test && make build`
5. Create GitHub release manually with release notes

## 📞 Support

- **Issues**: Use GitHub Issues for bug reports
- **Discussions**: Use GitHub Discussions for questions
- **Wiki**: Check project wiki for detailed guides
- **Releases**: Check releases page for latest versions

---

**Note**: Remember to replace `yourusername` with your actual GitHub username in all configuration files before pushing to GitHub. 