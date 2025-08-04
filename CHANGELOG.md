# Changelog

All notable changes to NeuraDocPrivacy will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Enhanced error handling for malformed PDF files
- Improved performance for large PDF documents
- Better support for different PDF encodings

### Changed
- Updated dependency versions for security improvements
- Refactored core masking algorithms for better accuracy

### Fixed
- Memory leak issues with large PDF processing
- Incorrect masking of certain email formats
- GUI responsiveness during long operations

## [1.2.0] - 2024-01-15

### Added
- **Batch Processing**: Process multiple PDF files simultaneously
- **Advanced Masking Styles**: 
  - Star masking (***)
  - Black box masking
  - Frame masking
- **Real-time Preview**: View PDF pages before and after masking
- **Command Line Interface**: Added CLI support for automation
- **Cross-platform Support**: Improved compatibility across Windows, macOS, and Linux
- **Modern GUI**: Complete UI redesign with PyQt5
- **Progress Indicators**: Real-time progress bars and status updates

### Changed
- **Complete UI Overhaul**: Modern, responsive interface design
- **Enhanced NLP Detection**: Improved accuracy of named entity recognition
- **Better Error Handling**: More informative error messages and recovery
- **Performance Optimization**: Faster processing of large documents
- **Documentation**: Comprehensive README and setup instructions

### Fixed
- Memory usage optimization for large PDF files
- Improved text extraction accuracy
- Better handling of complex PDF layouts
- Fixed issues with certain character encodings

## [1.1.0] - 2024-01-01

### Added
- **GUI Interface**: Basic PyQt5-based user interface
- **Multiple Masking Options**: 
  - Email addresses
  - Phone numbers
  - Personal names
  - Addresses
  - Organizations
  - Geographic locations
- **spaCy Integration**: Advanced NLP for named entity recognition
- **Configurable Masking**: User-selectable masking options

### Changed
- **Improved Text Detection**: Better regex patterns for various data types
- **Enhanced PDF Processing**: More robust PDF parsing and manipulation
- **Better Error Messages**: More descriptive error handling

### Fixed
- Issues with certain PDF formats
- Text extraction problems in complex layouts
- Memory management improvements

## [1.0.0] - 2023-12-15

### Added
- **Initial Release**: Basic PDF masking functionality
- **Core Features**:
  - PDF text extraction
  - Basic regex-based masking
  - Simple command-line interface
  - Support for common sensitive data types
- **Documentation**: Basic setup and usage instructions

### Changed
- N/A (Initial release)

### Fixed
- N/A (Initial release)

---

## Version History Summary

- **v1.0.0**: Basic functionality with command-line interface
- **v1.1.0**: Added GUI and enhanced masking capabilities
- **v1.2.0**: Complete overhaul with modern UI and batch processing
- **Unreleased**: Performance improvements and bug fixes

## Migration Guide

### From v1.1.0 to v1.2.0

The major changes in v1.2.0 include:

1. **New GUI**: The application now uses a modern PyQt5 interface
2. **Batch Processing**: You can now process multiple files at once
3. **Enhanced Masking**: New masking styles and improved accuracy
4. **Better Performance**: Optimized for larger files

### From v1.0.0 to v1.1.0

The transition from v1.0.0 to v1.1.0 introduced:

1. **GUI Interface**: Added PyQt5-based user interface
2. **Advanced NLP**: Integrated spaCy for better entity recognition
3. **More Masking Options**: Expanded beyond basic regex patterns

## Deprecation Notices

- **v1.3.0**: Some command-line arguments may be deprecated in favor of GUI options
- **v1.4.0**: Support for Python 3.7 will be dropped

## Known Issues

### Current Version (1.2.0)
- Large PDF files (>100MB) may take longer to process
- Some complex layouts might not mask perfectly
- OCR-processed PDFs may have limited accuracy

### Previous Versions
- **v1.1.0**: Memory issues with very large files (fixed in v1.2.0)
- **v1.0.0**: Limited text extraction capabilities (improved in v1.1.0)

## Future Roadmap

### Planned for v1.3.0
- [ ] OCR support for scanned documents
- [ ] Custom masking patterns
- [ ] Export/import configuration
- [ ] Plugin system for custom detectors

### Planned for v1.4.0
- [ ] Web interface
- [ ] API endpoints
- [ ] Cloud processing support
- [ ] Advanced analytics and reporting

### Long-term Goals
- [ ] Machine learning-based detection
- [ ] Multi-language support
- [ ] Integration with document management systems
- [ ] Real-time collaboration features 