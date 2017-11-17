---
UID: NF.mxdc.MxdcGetPDEVAdjustment
title: MxdcGetPDEVAdjustment
author: windows-driver-content
description: The MxdcGetPDEVAdjustment function is exported by a printer interface DLL and supplies printer configuration data for the Microsoft XPS Document Converter (MXDC).
old-location: print\mxdcgetpdevadjustment.htm
ms.assetid: 4839337b-0328-4919-8f49-d7847743845c
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: mxdc.h
req.include-header: Mxdc.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MxdcGetPDEVAdjustment
req.alt-loc: mxdc.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: MxdcGetPDEVAdjustment
req.iface: 
---

# MxdcGetPDEVAdjustment function



## -description
<p>The <code>MxdcGetPDEVAdjustment</code> function is exported by a printer interface DLL and supplies printer configuration data for the Microsoft XPS Document Converter (MXDC).</p>


## -syntax

````
HRESULT MxdcGetPDEVAdjustment(
  _In_           HANDLE                    hPrinter,
  _In_           ULONG                     cbDevMode,
  _In_     const DEVMODE                   *pDevMode,
  _In_           ULONG                     cbIn,
  _In_opt_ const VOID                      *pvIn,
  _In_           ULONG                     cbPrintPropertiesCollection,
  _Inout_        PrintPropertiesCollection *pOut
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>The handle of the currently instantiated printer.</p>
</dd>

### -param <i>cbDevMode</i> [in]

<dd>
<p>The size of the <a href="https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b">DEVMODE</a> structure, in bytes, including the driver's private DEVMODE data.</p>
</dd>

### -param <i>pDevMode</i> [in]

<dd>
<p>A copy of the DEVMODE structure that the MXDC received. The printer interface DLL uses information from this structure to return the requested data.</p>
</dd>

### -param <i>cbIn</i> [in]

<dd>
<p>An input parameter that designates the size of the <i>pvIn</i> parameter, in bytes. This parameter is currently not used and its value is zero.</p>
</dd>

### -param <i>pvIn</i> [in, optional]

<dd>
<p>A parameter that consists of data that is sent to the printer interface DLL from the MXDC. This parameter is currently not used and its value is <b>NULL</b>.</p>
</dd>

### -param <i>cbPrintPropertiesCollection</i> [in]

<dd>
<p>The size of the <a href="https://msdn.microsoft.com/240e14d1-d8ee-403c-b728-b14941775634">PrintPropertiesCollection</a> data structure, in bytes.</p>
</dd>

### -param <i>pOut</i> [in, out]

<dd>
<p>The <b>PrintPropertiesCollection</b> data structure from which the printer interface's DLL gets the requested data. This structure is defined in WinSpool.h. The requested fields might be pre-filled with the MXDC's default data. The printer interface DLL must ignore the fields that it does not understand.</p>
</dd>
</dl>

## -returns
<p><code>MxdcGetPDEVAdjustment</code> should return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The printer interface DLL successfully returned an adjusted imageable area, compression type, or DPI based on the given DEVMODE structure. The MXDC will validate the returned imageable area and then use it to populate the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566484">GDIINFO</a> structure to the respective fields.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The <code>MxdcGetPDEVAdjustment</code> function is not implemented by the printer interface. The printer interface must not modify the fields that it does not support. The MXDC defaults to its current defaults. For the imageable area case, MXDC defaults to using the physical page size. For the compression option, MXDC defaults to medium JPEG compression.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>For this value or any other failure values, the MXDC returns -1 to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a> function, catches the internal exception, and sets a flag to fail and end the print job.</p>

<p> </p>

## -remarks
<p>The <code>MxdcGetPDEVAdjustment</code> function is implemented by the hardware vendor. The MXDC calls this function to obtain printer configuration data in the form of a <a href="wdkgloss.p#wdkgloss.property_bag#wdkgloss.property_bag"><i>property bag</i></a> that includes the following data:</p>

<p></p><dl>
<dt><a id="Imageable_area"></a><a id="imageable_area"></a><a id="IMAGEABLE_AREA"></a>Imageable area</dt>
<dd>
<p>The corner coordinates of the area in which a printer can lay down ink, as determined by the design of the printer and the selected paper size.</p>
</dd>
<dt><a id="Image_compression_type"></a><a id="image_compression_type"></a><a id="IMAGE_COMPRESSION_TYPE"></a>Image compression type</dt>
<dd>
<p>The file format of an image, either JPEG or PNG, and the level of compression for JPEG images.</p>
</dd>
<dt><a id="Dots_per_inch_resolution"></a><a id="dots_per_inch_resolution"></a><a id="DOTS_PER_INCH_RESOLUTION"></a>Dots per inch resolution</dt>
<dd>
<p>The resolution of an image in dots per inch (DPI). If the printer interface DLL does not support this field, MXDC defaults to a device-independent resolution that the <b>dmPrintQuality</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure sets.</p>
</dd>
</dl><p>The corner coordinates of the area in which a printer can lay down ink, as determined by the design of the printer and the selected paper size.</p>

<p>The file format of an image, either JPEG or PNG, and the level of compression for JPEG images.</p>

<p>The resolution of an image in dots per inch (DPI). If the printer interface DLL does not support this field, MXDC defaults to a device-independent resolution that the <b>dmPrintQuality</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure sets.</p>

<p>MXDC enables the printer interface DLL to adjust DPI through the <code>MxdcGetPDEVAdjustment</code> function only if the print job's <b>dmPrintQuality</b> field has a value that is less than or equal to 0. If the DPI value is not adjusted, MXDC maps negative <b>dmPrintQuality</b> values to the following resolutions.</p>

<p>DMRES_HIGH</p>

<p>-4</p>

<p>2400</p>

<p>DMRES_MEDIUM</p>

<p>-3</p>

<p>1200</p>

<p>DMRES_LOW</p>

<p>-2</p>

<p>600</p>

<p>DMRES_DRAFT</p>

<p>-1</p>

<p>400</p>

<p> </p>

<p>The following table lists the MXDC's property types and property-bag fields for the properties.</p>

<p>L"MxdcImageableArea"</p>

<p>kPropertyTypeBuffer</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyBlob.cbBuf = sizeof(RECT)
       </p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyBlob.pBuf
       </p>

<p>L"MxdcImageCompressionType"</p>

<p>kPropertyTypeInt32</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyInt32
       </p>

<p>L"MxdcDotsPerInch"</p>

<p>kPropertyTypeInt32</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyInt32
       </p>

<p>L"MxdcLandscapeRotation" </p>

<p>kPropertyTypeInt32</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyInt32 
       </p>

<p> </p>

<p>The following table lists the MXDC's supported data types and data values for the properties.</p>

<p>L"MxdcImageableArea"</p>

<p>
        Data Type: RECT</p>

<p>
        Values:</p>

<p>RECT::left (Same as FORM_INFO_1)</p>

<p>RECT::right (Same as FORM_INFO_1)</p>

<p>RECT::top (Same as FORM_INFO_1)</p>

<p>RECT::bottom (Same as FORM_INFO_1)</p>

<p>L"MxdcImageCompressionType"</p>

<p>
        Data Type: LONG</p>

<p>
        Values:</p>

<p>1 = JPEG High Compression</p>

<p>2 = JPEG Medium Compression</p>

<p>3 = JPEG Low Compression</p>

<p>4 = PNG Compression</p>

<p>L"MxdcDotsPerInch"</p>

<p>
        Data Type: LONG</p>

<p>
        Values: </p>

<p>A positive value for Dots Per Inch</p>

<p>L"MxdcLandscapeRotation" </p>

<p>
        Data Type: LONG </p>

<p>Values:</p><dl>
<dd>90 = MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_90_DEGREES</dd>
<dd>0 = MXDC_LANDSCAPE_ROTATE_NONE</dd>
<dd>-90 = MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_270_DEGREES</dd>
</dl><p> </p>

<p>The <code>MxdcGetPDEVAdjustment</code> function is not a part of the MXDC. The MXDC calls back to this function in the driver's configuration DLL to obtain data for configuring the printer.</p>

<p>The MXDC expects the imageable area to be expressed in unrotated coordinates (portrait orientation). The MXDC rotates both the page size and the imageable area according to the value of the <b>dmOrientation</b> member of the DEVMODE structure pointed to by <i>pDevMode</i>. Thus, the hardware vendor's implementation of <code>MxdcGetPDEVAdjustment</code> should avoid specifying the imageable area in rotated coordinates (landscape orientation) because this will cause landscape print jobs to print incorrectly.</p>

<p>The default value in the MXDC will be MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_270_DEGREES, which is its current legacy behavior.</p>

<p>All rotation will be done on the imageable area. If a configuration component (UniDrv/PostScript, XPSDrv Monolithic) does not understand the new property bag values, then it should ignore them as is in the current design.</p>

<p>The <code>MxdcGetPDEVAdjustment</code> function is implemented by the hardware vendor. The MXDC calls this function to obtain printer configuration data in the form of a <a href="wdkgloss.p#wdkgloss.property_bag#wdkgloss.property_bag"><i>property bag</i></a> that includes the following data:</p>

<p></p><dl>
<dt><a id="Imageable_area"></a><a id="imageable_area"></a><a id="IMAGEABLE_AREA"></a>Imageable area</dt>
<dd>
<p>The corner coordinates of the area in which a printer can lay down ink, as determined by the design of the printer and the selected paper size.</p>
</dd>
<dt><a id="Image_compression_type"></a><a id="image_compression_type"></a><a id="IMAGE_COMPRESSION_TYPE"></a>Image compression type</dt>
<dd>
<p>The file format of an image, either JPEG or PNG, and the level of compression for JPEG images.</p>
</dd>
<dt><a id="Dots_per_inch_resolution"></a><a id="dots_per_inch_resolution"></a><a id="DOTS_PER_INCH_RESOLUTION"></a>Dots per inch resolution</dt>
<dd>
<p>The resolution of an image in dots per inch (DPI). If the printer interface DLL does not support this field, MXDC defaults to a device-independent resolution that the <b>dmPrintQuality</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure sets.</p>
</dd>
</dl><p>The corner coordinates of the area in which a printer can lay down ink, as determined by the design of the printer and the selected paper size.</p>

<p>The file format of an image, either JPEG or PNG, and the level of compression for JPEG images.</p>

<p>The resolution of an image in dots per inch (DPI). If the printer interface DLL does not support this field, MXDC defaults to a device-independent resolution that the <b>dmPrintQuality</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure sets.</p>

<p>MXDC enables the printer interface DLL to adjust DPI through the <code>MxdcGetPDEVAdjustment</code> function only if the print job's <b>dmPrintQuality</b> field has a value that is less than or equal to 0. If the DPI value is not adjusted, MXDC maps negative <b>dmPrintQuality</b> values to the following resolutions.</p>

<p>DMRES_HIGH</p>

<p>-4</p>

<p>2400</p>

<p>DMRES_MEDIUM</p>

<p>-3</p>

<p>1200</p>

<p>DMRES_LOW</p>

<p>-2</p>

<p>600</p>

<p>DMRES_DRAFT</p>

<p>-1</p>

<p>400</p>

<p> </p>

<p>The following table lists the MXDC's property types and property-bag fields for the properties.</p>

<p>L"MxdcImageableArea"</p>

<p>kPropertyTypeBuffer</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyBlob.cbBuf = sizeof(RECT)
       </p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyBlob.pBuf
       </p>

<p>L"MxdcImageCompressionType"</p>

<p>kPropertyTypeInt32</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyInt32
       </p>

<p>L"MxdcDotsPerInch"</p>

<p>kPropertyTypeInt32</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyInt32
       </p>

<p>L"MxdcLandscapeRotation" </p>

<p>kPropertyTypeInt32</p>

<p>
        PrintPropertiesCollection::propertiesCollection[i].propertyValue.value.propertyInt32 
       </p>

<p> </p>

<p>The following table lists the MXDC's supported data types and data values for the properties.</p>

<p>L"MxdcImageableArea"</p>

<p>
        Data Type: RECT</p>

<p>
        Values:</p>

<p>RECT::left (Same as FORM_INFO_1)</p>

<p>RECT::right (Same as FORM_INFO_1)</p>

<p>RECT::top (Same as FORM_INFO_1)</p>

<p>RECT::bottom (Same as FORM_INFO_1)</p>

<p>L"MxdcImageCompressionType"</p>

<p>
        Data Type: LONG</p>

<p>
        Values:</p>

<p>1 = JPEG High Compression</p>

<p>2 = JPEG Medium Compression</p>

<p>3 = JPEG Low Compression</p>

<p>4 = PNG Compression</p>

<p>L"MxdcDotsPerInch"</p>

<p>
        Data Type: LONG</p>

<p>
        Values: </p>

<p>A positive value for Dots Per Inch</p>

<p>L"MxdcLandscapeRotation" </p>

<p>
        Data Type: LONG </p>

<p>Values:</p><dl>
<dd>90 = MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_90_DEGREES</dd>
<dd>0 = MXDC_LANDSCAPE_ROTATE_NONE</dd>
<dd>-90 = MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_270_DEGREES</dd>
</dl><p> </p>

<p>The <code>MxdcGetPDEVAdjustment</code> function is not a part of the MXDC. The MXDC calls back to this function in the driver's configuration DLL to obtain data for configuring the printer.</p>

<p>The MXDC expects the imageable area to be expressed in unrotated coordinates (portrait orientation). The MXDC rotates both the page size and the imageable area according to the value of the <b>dmOrientation</b> member of the DEVMODE structure pointed to by <i>pDevMode</i>. Thus, the hardware vendor's implementation of <code>MxdcGetPDEVAdjustment</code> should avoid specifying the imageable area in rotated coordinates (landscape orientation) because this will cause landscape print jobs to print incorrectly.</p>

<p>The default value in the MXDC will be MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_270_DEGREES, which is its current legacy behavior.</p>

<p>All rotation will be done on the imageable area. If a configuration component (UniDrv/PostScript, XPSDrv Monolithic) does not understand the new property bag values, then it should ignore them as is in the current design.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mxdc.h (include Mxdc.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566484">GDIINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554157">IPrintOemUIMXDC Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20MxdcGetPDEVAdjustment function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
