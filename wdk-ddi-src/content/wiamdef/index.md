---
UID: NA:wiamdef
ms.assetid: d89bcd90-a043-33c1-b090-5984bd2940ed
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# wiamdef.h header



wiamdef.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [WIAS_ASSERT](nf-wiamdef-wias_assert.md) | The WIAS_ASSERT macro writes a diagnostic message to the Wiatrace.log file. |
| [WIAS_ERROR](nf-wiamdef-wias_error.md) | The WIAS_ERROR macro writes a diagnostic message to the Wiatrace.log file. |
| [WIAS_HRESULT](nf-wiamdef-wias_hresult.md) | The WIAS_HRESULT macro writes a diagnostic message to the Wiatrace.log file. |
| [WIAS_LERROR](nf-wiamdef-wias_lerror.md) | The WIAS_LERROR macro is obsolete for Windows Vista and later. It is recommended that the WIAS_ERROR macro be used instead.The WIAS_LERROR macro writes a diagnostic WIA_ERROR message to the log file. |
| [WIAS_LHRESULT](nf-wiamdef-wias_lhresult.md) | The WIAS_LHRESULT macro is obsolete for Windows Vista and later. It is recommended that the WIAS_HRESULT macro be used instead. The WIAS_LHRESULT macro translates an HRESULT value into a string and writes the string to the diagnostic log file. |
| [WIAS_LTRACE](nf-wiamdef-wias_ltrace.md) | The WIAS_LTRACE macro is obsolete for Windows Vista and later. It is recommended that the WIAS_TRACE macro be used instead.The WIAS_LTRACE macro writes a diagnostic WIA_TRACE message to the log file. |
| [WIAS_LWARNING](nf-wiamdef-wias_lwarning.md) | The WIAS_LWARNING macro is obsolete for Windows Vista and later.The WIAS_LWARNING macro writes a diagnostic WIA_WARNING message to the log file. |
| [WIAS_TRACE](nf-wiamdef-wias_trace.md) | The WIAS_TRACE macro writes a diagnostic message to the Wiatrace.log file. |
| [wiasCreateChildAppItem](nf-wiamdef-wiascreatechildappitem.md) | The wiasCreateChildAppItem function creates a new application item and inserts it as a child of the specified (parent) item. Note that this item will not have any properties in its property sets until the driver or application actually fills them in. |
| [wiasCreateDrvItem](nf-wiamdef-wiascreatedrvitem.md) | The wiasCreateDrvItem function creates an IWiaDrvItem Interface object. |
| [wiasCreateLogInstance](nf-wiamdef-wiascreateloginstance.md) | The wiasCreateLogInstance function creates an instance of a logging object. |
| [wiasCreatePropContext](nf-wiamdef-wiascreatepropcontext.md) | The wiasCreatePropContext function allocates a property context to indicate which of an item's properties are being changed by the application. |
| [wiasDebugError](nf-wiamdef-wiasdebugerror.md) | This function prints a debug error string in the Device Manager debug console. The output color is always red. |
| [wiasDebugTrace](nf-wiamdef-wiasdebugtrace.md) | This function prints a debug trace string in the Device Manager debug console. |
| [wiasDownSampleBuffer](nf-wiamdef-wiasdownsamplebuffer.md) | The wiasDownSampleBuffer function takes in a buffer of DWORD-aligned pixel data and downsamples it (produces image data of lower resolution) to the specified size and resolution. |
| [wiasFormatArgs](nf-wiamdef-wiasformatargs.md) | The wiasFormatArgs function formats an argument list into a packaged string for logging. |
| [wiasFreePropContext](nf-wiamdef-wiasfreepropcontext.md) | The wiasFreePropContext function releases the memory occupied by a WIA_PROPERTY_CONTEXT structure. |
| [wiasGetChangedValueFloat](nf-wiamdef-wiasgetchangedvaluefloat.md) | The wiasGetChangedValueFloat function determines whether a property with a floating-point value has been changed by an application. |
| [wiasGetChangedValueGuid](nf-wiamdef-wiasgetchangedvalueguid.md) | The wiasGetChangedValueGuid function determines whether a property with a GUID value has been changed by an application. |
| [wiasGetChangedValueLong](nf-wiamdef-wiasgetchangedvaluelong.md) | The wiasGetChangedValueLong function determines whether a property with a long integer value has been changed by an application. |
| [wiasGetChangedValueStr](nf-wiamdef-wiasgetchangedvaluestr.md) | The wiasGetChangedValueStr function determines whether a property with a string value has been changed by an application. |
| [wiasGetChildrenContexts](nf-wiamdef-wiasgetchildrencontexts.md) | The wiasGetChildrenContexts function retrieves an array of item contexts belonging to the current item's children. |
| [wiasGetContextFromName](nf-wiamdef-wiasgetcontextfromname.md) | The wiasGetContextFromName function retrieves the item context for an item name. |
| [wiasGetDrvItem](nf-wiamdef-wiasgetdrvitem.md) | The wiasGetDrvItem function retrieves a driver item. |
| [wiasGetImageInformation](nf-wiamdef-wiasgetimageinformation.md) | The wiasGetImageInformation function retrieves transfer context information from an item. |
| [wiasGetItemType](nf-wiamdef-wiasgetitemtype.md) | The wiasGetItemType function indicates the item type. |
| [wiasGetPropertyAttributes](nf-wiamdef-wiasgetpropertyattributes.md) | The wiasGetPropertyAttributes function retrieves the access flags and valid values for a set of properties. |
| [wiasGetRootItem](nf-wiamdef-wiasgetrootitem.md) | The wiasGetRootItem function retrieves the root item context of a specified WIA item. |
| [wiasIsPropChanged](nf-wiamdef-wiasispropchanged.md) | The wiasIsPropChanged function tests whether a specified property has been changed by an application. |
| [wiasParseEndorserString](nf-wiamdef-wiasparseendorserstring.md) | The wiasParseEndorserString function parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with those tokens. |
| [wiasPrintDebugHResult](nf-wiamdef-wiasprintdebughresult.md) | The wiasPrintDebugHResult function is obsolete for Windows XP and later, and is no longer supported. Use the WIAS_LHRESULT macro instead.This function prints an HRESULT string on the Device Manager debug console. |
| [wiasQueueEvent](nf-wiamdef-wiasqueueevent.md) | The wiasQueueEvent function informs the service that the device generated an event. |
| [wiasReadMultiple](nf-wiamdef-wiasreadmultiple.md) | The wiasReadMultiple function retrieves multiple property values from a WIA item. |
| [wiasReadPropBin](nf-wiamdef-wiasreadpropbin.md) | The wiasReadPropBin function retrieves a binary-data property value from a WIA item. |
| [wiasReadPropFloat](nf-wiamdef-wiasreadpropfloat.md) | The wiasReadPropFloat function retrieves a floating-point property value from a WIA item. |
| [wiasReadPropGuid](nf-wiamdef-wiasreadpropguid.md) | The wiasReadPropGuid function retrieves a GUID property value from a WIA item. |
| [wiasReadPropLong](nf-wiamdef-wiasreadproplong.md) | The wiasReadPropLong function retrieves a long integer property value from a WIA item. |
| [wiasReadPropStr](nf-wiamdef-wiasreadpropstr.md) | The wiasReadPropStr function retrieves a string property value from a WIA item. |
| [wiasSendEndOfPage](nf-wiamdef-wiassendendofpage.md) | The wiasSendEndOfPage function calls the client callback routine during a data transfer, sending the current total page count. |
| [wiasSetItemPropAttribs](nf-wiamdef-wiassetitempropattribs.md) | The wiasSetItemPropAttribs function sets the access flags and valid values for an item's set of properties. |
| [wiasSetItemPropNames](nf-wiamdef-wiassetitempropnames.md) | The wiasSetItemPropNames function writes property names to item properties. |
| [wiasSetPropChanged](nf-wiamdef-wiassetpropchanged.md) | The wiasSetPropChanged function modifies a property context to indicate that a property is being changed. |
| [wiasSetPropertyAttributes](nf-wiamdef-wiassetpropertyattributes.md) | The wiasSetPropertyAttributes function sets the access flags and valid values for a set of properties. |
| [wiasSetValidFlag](nf-wiamdef-wiassetvalidflag.md) | The wiasSetValidFlag function sets the valid values for a WIA_PROP_FLAG property. |
| [wiasSetValidListFloat](nf-wiamdef-wiassetvalidlistfloat.md) | The wiasSetValidListFloat function sets valid values for a WIA_PROP_LIST property of type VT_R4. |
| [wiasSetValidListGuid](nf-wiamdef-wiassetvalidlistguid.md) | The wiasSetValidListGuid function sets valid values for a WIA_PROP_LIST property of type VT_CLSID. |
| [wiasSetValidListLong](nf-wiamdef-wiassetvalidlistlong.md) | The wiasSetValidListLong function sets the valid values for a WIA_PROP_LIST property of type VT_I4. |
| [wiasSetValidListStr](nf-wiamdef-wiassetvalidliststr.md) | The wiasSetValidListStr function sets the valid values for a WIA_PROP_LIST property of type VT_BSTR. |
| [wiasSetValidRangeFloat](nf-wiamdef-wiassetvalidrangefloat.md) | The wiasSetValidRangeFloat function specifies the range of valid values for a WIA_PROP_RANGE property of type VT_R4. |
| [wiasSetValidRangeLong](nf-wiamdef-wiassetvalidrangelong.md) | The wiasSetValidRangeLong function specifies the range of valid values for a WIA_PROP_RANGE property of type VT_I4. |
| [wiasUpdateScanRect](nf-wiamdef-wiasupdatescanrect.md) | The wiasUpdateScanRect function updates the scanning area sizes of the scanning device. |
| [wiasUpdateValidFormat](nf-wiamdef-wiasupdatevalidformat.md) | The wiasUpdateValidFormat function updates the valid format of the property context for the current minidriver. |
| [wiasValidateItemProperties](nf-wiamdef-wiasvalidateitemproperties.md) | The wiasValidateItemProperties function validates a list of simple item properties against their current valid values. |
| [wiasWriteBufToFile](nf-wiamdef-wiaswritebuftofile.md) | The wiasWriteBufToFile function writes from a specified buffer to an image file. |
| [wiasWriteMultiple](nf-wiamdef-wiaswritemultiple.md) | The wiasWriteMultiple function writes multiple property values to a WIA item. |
| [wiasWritePageBufToFile](nf-wiamdef-wiaswritepagebuftofile.md) | The wiasWritePageBufToFile function writes the contents of a temporary page buffer to an image file. |
| [wiasWritePageBufToStream](nf-wiamdef-wiaswritepagebuftostream.md) | The wiasWritePageBufToStream function writes the contents of a temporary page buffer to the IStream interface provided by the application. |
| [wiasWritePropBin](nf-wiamdef-wiaswritepropbin.md) | The wiasWritePropBin function writes a single binary-data property value to a WIA item. |
| [wiasWritePropFloat](nf-wiamdef-wiaswritepropfloat.md) | The wiasWritePropFloat function writes a single floating-point property value to a WIA item. |
| [wiasWritePropGuid](nf-wiamdef-wiaswritepropguid.md) | The wiasWritePropGuid function writes a single GUID property value to a WIA item. |
| [wiasWritePropLong](nf-wiamdef-wiaswriteproplong.md) | The wiasWritePropLong function writes a single long integer property value to a WIA item. |
| [wiasWritePropStr](nf-wiamdef-wiaswritepropstr.md) | The wiasWritePropStr function writes a single string property value to a WIA item. |