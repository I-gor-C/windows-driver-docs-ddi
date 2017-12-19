---
UID: NA:
---

# Wiautil.h header

## -description

This header is used by Image. For more information, see
- [Image](../_Image/index.md)

Wiautil.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [wiauDbgDump function](nf-wiautil-wiaudbgdump.md) | The wiauDbgDump function logs a message containing one or more data values. |
| [wiauDbgError function](nf-wiautil-wiaudbgerror.md) | The wiauDbgError function logs an error message. |
| [wiauDbgErrorHr function](nf-wiautil-wiaudbgerrorhr.md) | The wiauDbgErrorHr function logs a message containing an HRESULT and its error message string. |
| [wiauDbgFlags function](nf-wiautil-wiaudbgflags.md) | The wiauDbgFlags function determines whether a particular debugging flag is set. |
| [wiauDbgHelper function](nf-wiautil-wiaudbghelper.md) | The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both. |
| [wiauDbgHelper2 function](nf-wiautil-wiaudbghelper2.md) | The wiauDbgHelper2 function writes a message to a log file, or debugger, or both. |
| [wiauDbgInit function](nf-wiautil-wiaudbginit.md) | The wiauDbgInit function initializes WIA debugging. |
| [wiauDbgLegacyError function](nf-wiautil-wiaudbglegacyerror.md) | The wiauDbgLegacyError function logs an error message. |
| [wiauDbgLegacyError2 function](nf-wiautil-wiaudbglegacyerror2.md) | The wiauDbgLegacyError2 function logs an error message. |
| [wiauDbgLegacyHresult2 function](nf-wiautil-wiaudbglegacyhresult2.md) | The wiauDbgLegacyHresult2 function logs a default message containing an HRESULT. |
| [wiauDbgLegacyTrace function](nf-wiautil-wiaudbglegacytrace.md) | The wiauDbgLegacyTrace function logs a trace message. |
| [wiauDbgLegacyTrace2 function](nf-wiautil-wiaudbglegacytrace2.md) | The wiauDbgLegacyTrace2 function logs a trace message. |
| [wiauDbgLegacyWarning function](nf-wiautil-wiaudbglegacywarning.md) | The wiauDbgLegacyWarning function logs a warning message. |
| [wiauDbgSetFlags function](nf-wiautil-wiaudbgsetflags.md) | The wiauDbgSetFlags function sets debugging flags. |
| [wiauDbgTrace function](nf-wiautil-wiaudbgtrace.md) | The wiauDbgTrace function logs a trace message. |
| [wiauDbgWarning function](nf-wiautil-wiaudbgwarning.md) | The wiauDbgWarning function logs a warning message. |
| [wiauGetDrvItemContext function](nf-wiautil-wiaugetdrvitemcontext.md) | The wiauGetDrvItemContext function gets the driver item context, and optionally, the driver item. |
| [wiauGetDrvItemContext function](nf-wiautil-wiaugetdrvitemcontext~r1.md) | The wiauGetDrvItemContext function gets the driver item context, and optionally, the driver item. |
| [wiauGetResourceString function](nf-wiautil-wiaugetresourcestring.md) | The wiauGetResourceString function gets a resource string, storing it as a BSTR. |
| [wiauGetResourceString function](nf-wiautil-wiaugetresourcestring~r1.md) | The wiauGetResourceString function gets a resource string, storing it as a BSTR. |
| [wiauGetValidFormats function](nf-wiautil-wiaugetvalidformats.md) | The wiauGetValidFormats function calls the IWiaMiniDrv |
| [wiauGetValidFormats function](nf-wiautil-wiaugetvalidformats~r1.md) | The wiauGetValidFormats function calls the IWiaMiniDrv |
| [wiauPropInPropSpec function](nf-wiautil-wiaupropinpropspec.md) | The wiauPropInPropSpec function determines whether a specified property specification ID is contained in an array of such values. The function optionally gets the index at which the property specification ID was found. |
| [wiauPropInPropSpec function](nf-wiautil-wiaupropinpropspec~r1.md) | The wiauPropInPropSpec function determines whether a specified property specification ID is contained in an array of such values. The function optionally gets the index at which the property specification ID was found. |
| [wiauPropsInPropSpec function](nf-wiautil-wiaupropsinpropspec.md) | The wiauPropsInPropSpec function determines whether any of a list of property specification IDs is contained within an array of such values. |
| [wiauPropsInPropSpec function](nf-wiautil-wiaupropsinpropspec~r1.md) | The wiauPropsInPropSpec function determines whether any of a list of property specification IDs is contained within an array of such values. |
| [wiauSetImageItemSize function](nf-wiautil-wiausetimageitemsize.md) | The wiauSetImageItemSize function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties. |
| [wiauSetImageItemSize function](nf-wiautil-wiausetimageitemsize~r1.md) | The wiauSetImageItemSize function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties. |
| [wiauStrC2C function](nf-wiautil-wiaustrc2c.md) | The wiauStrC2C function copies an ANSI character string to another ANSI character string. |
| [wiauStrC2C function](nf-wiautil-wiaustrc2c~r1.md) | The wiauStrC2C function copies an ANSI character string to another ANSI character string. |
| [wiauStrC2W function](nf-wiautil-wiaustrc2w.md) | The wiauStrC2W function converts an ANSI character string to a Unicode string. |
| [wiauStrC2W function](nf-wiautil-wiaustrc2w~r1.md) | The wiauStrC2W function converts an ANSI character string to a Unicode string. |
| [wiauStrW2C function](nf-wiautil-wiaustrw2c.md) | The wiauStrW2C function converts a Unicode string to an ANSI character string. |
| [wiauStrW2C function](nf-wiautil-wiaustrw2c~r1.md) | The wiauStrW2C function converts a Unicode string to an ANSI character string. |
| [wiauStrW2W function](nf-wiautil-wiaustrw2w.md) | The wiauStrW2W function copies a Unicode string to another Unicode string. |
| [wiauStrW2W function](nf-wiautil-wiaustrw2w~r1.md) | The wiauStrW2W function copies a Unicode string to another Unicode string. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_BMP_IMAGE_INFO structure](ns-wiautil-_bmp_image_info.md) | The BMP_IMAGE_INFO structure contains information about a BMP image. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [SKIP_AMOUNT enumeration](ne-wiautil-skip_amount.md) | The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over. |

## Macros

| Title   | Description   |
| ---- |:---- |
| [wiauDbgHelper macro](nf-wiautil-wiaudbghelper~r1.md) | The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both. |
| [wiauDbgInit macro](nf-wiautil-wiaudbginit~r1.md) | The wiauDbgInit function initializes WIA debugging. |
| [wiauDbgSetFlags macro](nf-wiautil-wiaudbgsetflags~r1.md) | The wiauDbgSetFlags function sets debugging flags. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [CWiauDbgFn::CWiauDbgFn method](nf-wiautil-cwiaudbgfn-cwiaudbgfn.md) | The CWiauDbgFn |
| [CWiauDbgFn::~CWiauDbgFn method](nf-wiautil-cwiaudbgfn-~cwiaudbgfn.md) | The CWiauDbgFn |
| [CWiauFormatConverter::CWiauFormatConverter method](nf-wiautil-cwiauformatconverter-cwiauformatconverter.md) | The CWiauFormatConverter |
| [CWiauFormatConverter::ConvertToBmp method](nf-wiautil-cwiauformatconverter-converttobmp.md) | The CWiauFormatConverter |
| [CWiauFormatConverter::Init method](nf-wiautil-cwiauformatconverter-init.md) | The CWiauFormatConverter |
| [CWiauFormatConverter::IsFormatSupported method](nf-wiautil-cwiauformatconverter-isformatsupported.md) | The CWiauFormatConverter |
| [CWiauFormatConverter::~CWiauFormatConverter method](nf-wiautil-cwiauformatconverter-~cwiauformatconverter.md) | The CWiauFormatConverter |
| [CWiauPropertyList::CWiauPropertyList method](nf-wiautil-cwiaupropertylist-cwiaupropertylist.md) | The CWiauPropertyList |
| [CWiauPropertyList::DefineProperty method](nf-wiautil-cwiaupropertylist-defineproperty.md) | The CWiauPropertyList |
| [CWiauPropertyList::GetPropId method](nf-wiautil-cwiaupropertylist-getpropid.md) | The CWiauPropertyList |
| [CWiauPropertyList::Init method](nf-wiautil-cwiaupropertylist-init.md) | The CWiauPropertyList |
| [CWiauPropertyList::LookupPropId method](nf-wiautil-cwiaupropertylist-lookuppropid.md) | The CWiauPropertyList |
| [CWiauPropertyList::SendToWia method](nf-wiautil-cwiaupropertylist-sendtowia.md) | The CWiauPropertyList |
| [CWiauPropertyList::SetAccessSubType method](nf-wiautil-cwiaupropertylist-setaccesssubtype.md) | The CWiauPropertyList |
| [CWiauPropertyList::SetAccessSubType method](nf-wiautil-cwiaupropertylist-setaccesssubtype~r1.md) | The CWiauPropertyList |
| [CWiauPropertyList::~CWiauPropertyList method](nf-wiautil-cwiaupropertylist-~cwiaupropertylist.md) | The CWiauPropertyList |
