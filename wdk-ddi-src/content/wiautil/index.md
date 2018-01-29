---
UID : NA:wiautil
ms.assetid : 772a15b8-8c34-3cf7-8c3b-dca823285720
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wiautil.h header



wiautil.h contains the following programming interfaces:


## Classes
| Title | Description |
| ---- |:---- |
| [CWiauDbgFn](nl-wiautil-cwiaudbgfn.md) | The CWiauDbgFn class is a helper class that is used for tracing function or method entry and exit points. |
| [CWiauFormatConverter](nl-wiautil-cwiauformatconverter.md) | The CWiauFormatConverter class is a helper class for converting images to BMP format. |
| [CWiauPropertyList](nl-wiautil-cwiaupropertylist.md) | The CWiauPropertyList class can be used to create and maintain a list of properties for a device. |




## Functions
| Title | Description |
| ---- |:---- |
| [wiauDbgDump](nf-wiautil-wiaudbgdump.md) | The wiauDbgDump function logs a message containing one or more data values. |
| [wiauDbgError](nf-wiautil-wiaudbgerror.md) | The wiauDbgError function logs an error message. |
| [wiauDbgErrorHr](nf-wiautil-wiaudbgerrorhr.md) | The wiauDbgErrorHr function logs a message containing an HRESULT and its error message string. |
| [wiauDbgFlags](nf-wiautil-wiaudbgflags.md) | The wiauDbgFlags function determines whether a particular debugging flag is set. |
| [wiauDbgHelper](nf-wiautil-wiaudbghelper.md) | The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both. |
| [wiauDbgHelper2](nf-wiautil-wiaudbghelper2.md) | The wiauDbgHelper2 function writes a message to a log file, or debugger, or both. |
| [wiauDbgInit](nf-wiautil-wiaudbginit.md) | The wiauDbgInit function initializes WIA debugging. |
| [wiauDbgLegacyError](nf-wiautil-wiaudbglegacyerror.md) | The wiauDbgLegacyError function logs an error message. |
| [wiauDbgLegacyError2](nf-wiautil-wiaudbglegacyerror2.md) | The wiauDbgLegacyError2 function logs an error message. |
| [wiauDbgLegacyHresult2](nf-wiautil-wiaudbglegacyhresult2.md) | The wiauDbgLegacyHresult2 function logs a default message containing an HRESULT. |
| [wiauDbgLegacyTrace](nf-wiautil-wiaudbglegacytrace.md) | The wiauDbgLegacyTrace function logs a trace message. |
| [wiauDbgLegacyTrace2](nf-wiautil-wiaudbglegacytrace2.md) | The wiauDbgLegacyTrace2 function logs a trace message. |
| [wiauDbgLegacyWarning](nf-wiautil-wiaudbglegacywarning.md) | The wiauDbgLegacyWarning function logs a warning message. |
| [wiauDbgSetFlags](nf-wiautil-wiaudbgsetflags.md) | The wiauDbgSetFlags function sets debugging flags. |
| [wiauDbgTrace](nf-wiautil-wiaudbgtrace.md) | The wiauDbgTrace function logs a trace message. |
| [wiauDbgWarning](nf-wiautil-wiaudbgwarning.md) | The wiauDbgWarning function logs a warning message. |
| [wiauGetDrvItemContext](nf-wiautil-wiaugetdrvitemcontext.md) | The wiauGetDrvItemContext function gets the driver item context, and optionally, the driver item. |
| [wiauGetResourceString](nf-wiautil-wiaugetresourcestring.md) | The wiauGetResourceString function gets a resource string, storing it as a BSTR. |
| [wiauGetValidFormats](nf-wiautil-wiaugetvalidformats.md) | The wiauGetValidFormats function calls the IWiaMiniDrv::drvGetWiaFormatInfo method and makes a list of valid formats, using a specified tymed value. |
| [wiauPropInPropSpec](nf-wiautil-wiaupropinpropspec.md) | The wiauPropInPropSpec function determines whether a specified property specification ID is contained in an array of such values. The function optionally gets the index at which the property specification ID was found. |
| [wiauPropsInPropSpec](nf-wiautil-wiaupropsinpropspec.md) | The wiauPropsInPropSpec function determines whether any of a list of property specification IDs is contained within an array of such values. |
| [wiauSetImageItemSize](nf-wiautil-wiausetimageitemsize.md) | The wiauSetImageItemSize function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties. |
| [wiauStrC2C](nf-wiautil-wiaustrc2c.md) | The wiauStrC2C function copies an ANSI character string to another ANSI character string. |
| [wiauStrC2W](nf-wiautil-wiaustrc2w.md) | The wiauStrC2W function converts an ANSI character string to a Unicode string. |
| [wiauStrW2C](nf-wiautil-wiaustrw2c.md) | The wiauStrW2C function converts a Unicode string to an ANSI character string. |
| [wiauStrW2W](nf-wiautil-wiaustrw2w.md) | The wiauStrW2W function copies a Unicode string to another Unicode string. |



## Structures
| Title | Description |
| ---- |:---- |
| [_BMP_IMAGE_INFO](ns-wiautil-_bmp_image_info.md) | The BMP_IMAGE_INFO structure contains information about a BMP image. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [SKIP_AMOUNT](ne-wiautil-skip_amount.md) | The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over. |