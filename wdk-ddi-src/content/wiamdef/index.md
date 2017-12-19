---
UID: NA:
---

# Wiamdef.h header

## -description

This header is used by Image. For more information, see
- [Image](../_Image/index.md)

Wiamdef.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [wiasCreateChildAppItem function](nf-wiamdef-wiascreatechildappitem.md) | The wiasCreateChildAppItem function creates a new application item and inserts it as a child of the specified (parent) item. Note that this item will not have any properties in its property sets until the driver or application actually fills them in. |
| [wiasCreateDrvItem function](nf-wiamdef-wiascreatedrvitem.md) | The wiasCreateDrvItem function creates an IWiaDrvItem Interface object. |
| [wiasCreateLogInstance function](nf-wiamdef-wiascreateloginstance.md) | The wiasCreateLogInstance function creates an instance of a logging object. |
| [wiasCreatePropContext function](nf-wiamdef-wiascreatepropcontext.md) | The wiasCreatePropContext function allocates a property context to indicate which of an item's properties are being changed by the application. |
| [wiasDebugError function](nf-wiamdef-wiasdebugerror.md) | This function prints a debug error string in the Device Manager debug console. The output color is always red. |
| [wiasDebugTrace function](nf-wiamdef-wiasdebugtrace.md) | This function prints a debug trace string in the Device Manager debug console. |
| [wiasDownSampleBuffer function](nf-wiamdef-wiasdownsamplebuffer.md) | The wiasDownSampleBuffer function takes in a buffer of DWORD-aligned pixel data and downsamples it (produces image data of lower resolution) to the specified size and resolution. |
| [wiasFormatArgs function](nf-wiamdef-wiasformatargs.md) | The wiasFormatArgs function formats an argument list into a packaged string for logging. |
| [wiasFreePropContext function](nf-wiamdef-wiasfreepropcontext.md) | The wiasFreePropContext function releases the memory occupied by a WIA_PROPERTY_CONTEXT structure. |
| [wiasGetChangedValueFloat function](nf-wiamdef-wiasgetchangedvaluefloat.md) | The wiasGetChangedValueFloat function determines whether a property with a floating-point value has been changed by an application. |
| [wiasGetChangedValueGuid function](nf-wiamdef-wiasgetchangedvalueguid.md) | The wiasGetChangedValueGuid function determines whether a property with a GUID value has been changed by an application. |
| [wiasGetChangedValueLong function](nf-wiamdef-wiasgetchangedvaluelong.md) | The wiasGetChangedValueLong function determines whether a property with a long integer value has been changed by an application. |
| [wiasGetChangedValueStr function](nf-wiamdef-wiasgetchangedvaluestr.md) | The wiasGetChangedValueStr function determines whether a property with a string value has been changed by an application. |
| [wiasGetChildrenContexts function](nf-wiamdef-wiasgetchildrencontexts.md) | The wiasGetChildrenContexts function retrieves an array of item contexts belonging to the current item's children. |
| [wiasGetContextFromName function](nf-wiamdef-wiasgetcontextfromname.md) | The wiasGetContextFromName function retrieves the item context for an item name. |
| [wiasGetDrvItem function](nf-wiamdef-wiasgetdrvitem.md) | The wiasGetDrvItem function retrieves a driver item. |
| [wiasGetImageInformation function](nf-wiamdef-wiasgetimageinformation.md) | The wiasGetImageInformation function retrieves transfer context information from an item. |
| [wiasGetItemType function](nf-wiamdef-wiasgetitemtype.md) | The wiasGetItemType function indicates the item type. |
| [wiasGetPropertyAttributes function](nf-wiamdef-wiasgetpropertyattributes.md) | The wiasGetPropertyAttributes function retrieves the access flags and valid values for a set of properties. |
| [wiasGetRootItem function](nf-wiamdef-wiasgetrootitem.md) | The wiasGetRootItem function retrieves the root item context of a specified WIA item. |
| [wiasIsPropChanged function](nf-wiamdef-wiasispropchanged.md) | The wiasIsPropChanged function tests whether a specified property has been changed by an application. |
| [wiasParseEndorserString function](nf-wiamdef-wiasparseendorserstring.md) | The wiasParseEndorserString function parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with those tokens. |
| [wiasPrintDebugHResult function](nf-wiamdef-wiasprintdebughresult.md) | The wiasPrintDebugHResult function is obsolete for Windows XP and later, and is no longer supported. Use the WIAS_LHRESULT macro instead.This function prints an HRESULT string on the Device Manager debug console. |
| [wiasQueueEvent function](nf-wiamdef-wiasqueueevent.md) | The wiasQueueEvent function informs the service that the device generated an event. |
| [wiasReadMultiple function](nf-wiamdef-wiasreadmultiple.md) | The wiasReadMultiple function retrieves multiple property values from a WIA item. |
| [wiasReadPropBin function](nf-wiamdef-wiasreadpropbin.md) | The wiasReadPropBin function retrieves a binary-data property value from a WIA item. |
| [wiasReadPropFloat function](nf-wiamdef-wiasreadpropfloat.md) | The wiasReadPropFloat function retrieves a floating-point property value from a WIA item. |
| [wiasReadPropGuid function](nf-wiamdef-wiasreadpropguid.md) | The wiasReadPropGuid function retrieves a GUID property value from a WIA item. |
| [wiasReadPropLong function](nf-wiamdef-wiasreadproplong.md) | The wiasReadPropLong function retrieves a long integer property value from a WIA item. |
| [wiasReadPropStr function](nf-wiamdef-wiasreadpropstr.md) | The wiasReadPropStr function retrieves a string property value from a WIA item. |
| [wiasSendEndOfPage function](nf-wiamdef-wiassendendofpage.md) | The wiasSendEndOfPage function calls the client callback routine during a data transfer, sending the current total page count. |
| [wiasSetItemPropAttribs function](nf-wiamdef-wiassetitempropattribs.md) | The wiasSetItemPropAttribs function sets the access flags and valid values for an item's set of properties. |
| [wiasSetItemPropNames function](nf-wiamdef-wiassetitempropnames.md) | The wiasSetItemPropNames function writes property names to item properties. |
| [wiasSetPropChanged function](nf-wiamdef-wiassetpropchanged.md) | The wiasSetPropChanged function modifies a property context to indicate that a property is being changed. |
| [wiasSetPropertyAttributes function](nf-wiamdef-wiassetpropertyattributes.md) | The wiasSetPropertyAttributes function sets the access flags and valid values for a set of properties. |
| [wiasSetValidFlag function](nf-wiamdef-wiassetvalidflag.md) | The wiasSetValidFlag function sets the valid values for a WIA_PROP_FLAG property. |
| [wiasSetValidListFloat function](nf-wiamdef-wiassetvalidlistfloat.md) | The wiasSetValidListFloat function sets valid values for a WIA_PROP_LIST property of type VT_R4. |
| [wiasSetValidListGuid function](nf-wiamdef-wiassetvalidlistguid.md) | The wiasSetValidListGuid function sets valid values for a WIA_PROP_LIST property of type VT_CLSID. |
| [wiasSetValidListLong function](nf-wiamdef-wiassetvalidlistlong.md) | The wiasSetValidListLong function sets the valid values for a WIA_PROP_LIST property of type VT_I4. |
| [wiasSetValidListStr function](nf-wiamdef-wiassetvalidliststr.md) | The wiasSetValidListStr function sets the valid values for a WIA_PROP_LIST property of type VT_BSTR. |
| [wiasSetValidRangeFloat function](nf-wiamdef-wiassetvalidrangefloat.md) | The wiasSetValidRangeFloat function specifies the range of valid values for a WIA_PROP_RANGE property of type VT_R4. |
| [wiasSetValidRangeLong function](nf-wiamdef-wiassetvalidrangelong.md) | The wiasSetValidRangeLong function specifies the range of valid values for a WIA_PROP_RANGE property of type VT_I4. |
| [wiasUpdateScanRect function](nf-wiamdef-wiasupdatescanrect.md) | The wiasUpdateScanRect function updates the scanning area sizes of the scanning device. |
| [wiasUpdateValidFormat function](nf-wiamdef-wiasupdatevalidformat.md) | The wiasUpdateValidFormat function updates the valid format of the property context for the current minidriver. |
| [wiasValidateItemProperties function](nf-wiamdef-wiasvalidateitemproperties.md) | The wiasValidateItemProperties function validates a list of simple item properties against their current valid values. |
| [wiasWriteBufToFile function](nf-wiamdef-wiaswritebuftofile.md) | The wiasWriteBufToFile function writes from a specified buffer to an image file. |
| [wiasWriteMultiple function](nf-wiamdef-wiaswritemultiple.md) | The wiasWriteMultiple function writes multiple property values to a WIA item. |
| [wiasWritePageBufToFile function](nf-wiamdef-wiaswritepagebuftofile.md) | The wiasWritePageBufToFile function writes the contents of a temporary page buffer to an image file. |
| [wiasWritePageBufToStream function](nf-wiamdef-wiaswritepagebuftostream.md) | The wiasWritePageBufToStream function writes the contents of a temporary page buffer to the IStream interface provided by the application. |
| [wiasWritePropBin function](nf-wiamdef-wiaswritepropbin.md) | The wiasWritePropBin function writes a single binary-data property value to a WIA item. |
| [wiasWritePropFloat function](nf-wiamdef-wiaswritepropfloat.md) | The wiasWritePropFloat function writes a single floating-point property value to a WIA item. |
| [wiasWritePropGuid function](nf-wiamdef-wiaswritepropguid.md) | The wiasWritePropGuid function writes a single GUID property value to a WIA item. |
| [wiasWritePropLong function](nf-wiamdef-wiaswriteproplong.md) | The wiasWritePropLong function writes a single long integer property value to a WIA item. |
| [wiasWritePropStr function](nf-wiamdef-wiaswritepropstr.md) | The wiasWritePropStr function writes a single string property value to a WIA item. |

## Macros

| Title   | Description   |
| ---- |:---- |
| [WIAS_ASSERT macro](nf-wiamdef-wias_assert.md) | The WIAS_ASSERT macro writes a diagnostic message to the Wiatrace.log file. |
| [WIAS_ERROR macro](nf-wiamdef-wias_error.md) | The WIAS_ERROR macro writes a diagnostic message to the Wiatrace.log file. |
| [WIAS_HRESULT macro](nf-wiamdef-wias_hresult.md) | The WIAS_HRESULT macro writes a diagnostic message to the Wiatrace.log file. |
| [WIAS_LERROR macro](nf-wiamdef-wias_lerror.md) | The WIAS_LERROR macro is obsolete for Windows Vista and later. It is recommended that the WIAS_ERROR macro be used instead.The WIAS_LERROR macro writes a diagnostic WIA_ERROR message to the log file. |
| [WIAS_LHRESULT macro](nf-wiamdef-wias_lhresult.md) | The WIAS_LHRESULT macro is obsolete for Windows Vista and later. It is recommended that the WIAS_HRESULT macro be used instead. The WIAS_LHRESULT macro translates an HRESULT value into a string and writes the string to the diagnostic log file. |
| [WIAS_LTRACE macro](nf-wiamdef-wias_ltrace.md) | The WIAS_LTRACE macro is obsolete for Windows Vista and later. It is recommended that the WIAS_TRACE macro be used instead.The WIAS_LTRACE macro writes a diagnostic WIA_TRACE message to the log file. |
| [WIAS_LWARNING macro](nf-wiamdef-wias_lwarning.md) | The WIAS_LWARNING macro is obsolete for Windows Vista and later.The WIAS_LWARNING macro writes a diagnostic WIA_WARNING message to the log file. |
| [WIAS_TRACE macro](nf-wiamdef-wias_trace.md) | The WIAS_TRACE macro writes a diagnostic message to the Wiatrace.log file. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [CWiaLogProc::CWiaLogProc method](nf-wiamdef-cwialogproc-cwialogproc.md) | The CWiaLogProc constructor is called when the function or method being logged is entered. |
| [CWiaLogProc::~CWiaLogProc method](nf-wiamdef-cwialogproc-~cwialogproc.md) | The ~CWiaLogProc destructor is called when the function or method being logged is exited. |
| [CWiaLogProcEx::CWiaLogProcEx method](nf-wiamdef-cwialogprocex-cwialogprocex.md) | The CWiaLogProcEx constructor is called when the function or method being logged is entered. |
| [CWiaLogProcEx::~CWiaLogProcEx method](nf-wiamdef-cwialogprocex-~cwialogprocex.md) | The~CWiaLogProcEx destructor is called when the function or method being logged is exited. |
