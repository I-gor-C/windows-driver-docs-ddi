---
UID: NF.winddiui.DrvDeviceCapabilities
title: DrvDeviceCapabilities
author: windows-driver-content
description: A printer interface DLL's DrvDeviceCapabilities function returns requested information about a printer's capabilities.
old-location: print\drvdevicecapabilities.htm
ms.assetid: a8ea236d-42f9-45c5-b2f6-035e0ba28f75
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrvDeviceCapabilities
req.alt-loc: winddiui.h
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
ms.keywords: DrvDeviceCapabilities
req.iface: 
req.product: Windows 10 or later.
---

# DrvDeviceCapabilities function



## -description
<p>A printer interface DLL's <b>DrvDeviceCapabilities</b> function returns requested information about a printer's capabilities.</p>


## -syntax

````
DWORD DrvDeviceCapabilities(
        HANDLE   hPrinter,
  _In_  PWSTR    pDeviceName,
        WORD     iDevCap,
  _Out_ PVOID    pvOutput,
  _In_  PDEVMODE pDevMode
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> 

<dd>
<p>Caller-supplied printer handle.</p>
</dd>

### -param <i>pDeviceName</i> [in]

<dd>
<p>Caller-supplied pointer to a printer name string.</p>
</dd>

### -param <i>iDevCap</i> 

<dd>
<p>Caller-supplied bit flag indicating the information being requested. This can be one of the flags listed in the following table. (The flags are defined in header file Wingdi.h.)</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DC_BINADJUST</p>
</td>
<td>
<p>Not used for NT-based operating systems.</p>
</td>
</tr>
<tr>
<td>
<p>DC_BINNAMES</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with an array of string buffers, each 24 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a paper source bin.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_BINS</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with a WORD array. Each array element should contain a DMBIN-prefixed constant (or customized value) representing a supported paper source bin.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_COLLATE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be 1 if the printer supports collating; otherwise, the return value should be zero.</p>
</td>
</tr>
<tr>
<td>
<p>DC_COLORDEVICE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be 1 if the printer supports color printing; otherwise, the return value should be zero.</p>
</td>
</tr>
<tr>
<td>
<p>DC_COPIES</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the maximum number of copies the printer can support.</p>
</td>
</tr>
<tr>
<td>
<p>DC_DATATYPE_PRODUCED</p>
</td>
<td>
<p>Not used for NT-based operating systems.</p>
</td>
</tr>
<tr>
<td>
<p>DC_DRIVER</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the <b>dmDriverVersion</b> member of the driver's internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>DC_DUPLEX</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be 1 if the printer supports duplex printing; otherwise, the return value should be zero.</p>
</td>
</tr>
<tr>
<td>
<p>DC_EMF_COMPLIANT</p>
</td>
<td>
<p>Not used for NT-based operating systems.</p>
</td>
</tr>
<tr>
<td>
<p>DC_ENUMRESOLUTIONS</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with a LONG array. For each resolution supported by the printer, the function should return two long words (one for the <i>x</i> dimension and one for the <i>y</i> dimension) of the resolution, in dots per inch.</p>
<p>The function's return value should be the number of resolutions supported.</p>
<p>If <b>pvOutput</b> is <b>NULL</b>, the function should just return the number of resolutions supported.</p>
</td>
</tr>
<tr>
<td>
<p>DC_EXTRA</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the <b>dmDriverExtra</b> member of the driver's internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>DC_FIELDS</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the <b>dmFields</b> member of the driver's internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure. The <b>dmFields</b> member indicates which members in the device-independent portion of the DEVMODEW structure are supported by the printer driver.</p>
</td>
</tr>
<tr>
<td>
<p>DC_FILEDEPENDENCIES</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a file that must be installed with the driver.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MANUFACTURER</p>
</td>
<td>
<p>Not used for NT-based operating systems.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MAXEXTENT</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function should return a POINTS structure (described in the Microsoft Windows SDK documentation). The structure should contain the maximum allowable values for the <b>dmPaperWidth</b> (<i>x</i> dimension) and <b>dmPaperLength</b> (<i>y</i> dimension) members of the printer's DEVMODEW structure.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MEDIAREADY</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a paper form that is available for use.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MEDIATYPENAMES</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a supported media type. </p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should simply return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MEDIATYPES</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with a DWORD array. Each array element should contain a DMMEDIA-prefixed constant (see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure) or customized value representing a supported media type. </p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should simply return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MINEXTENT</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function should return a POINTS structure (described in the Windows SDK documentation). The structure should contain the minimum allowable values for the <b>dmPaperWidth</b> (<i>x</i> dimension) and <b>dmPaperLength</b> (<i>y</i> dimension) members of the printer's DEVMODEW structure.</p>
</td>
</tr>
<tr>
<td>
<p>DC_MODEL</p>
</td>
<td>
<p>Not used for NT-based operating systems.</p>
</td>
</tr>
<tr>
<td>
<p>DC_NUP</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with a DWORD array. Each array element should contain an integer representing an N-up option (that is, each integer should represent a supported number of document pages per physical page).</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_ORIENTATION</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the number of degrees of rotation required to produce landscape orientation from portrait orientation. A value of zero indicates landscape orientation is not supported.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PAPERNAMES</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a paper form.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PAPERS</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with a WORD array. Each array element should contain a DMPAPER-prefixed constant (or customized value) representing a supported paper form.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PAPERSIZE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with a POINT array. Each array element should contain the <i>x</i> and <i>y</i> dimensions of a form's paper size, in 0.1 mm units, in portrait orientation.</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PERSONALITY</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter points to a buffer that the function should fill with an array of string buffers, each 32 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the printer description language supported by the printer (for example, L"HP-GL/2").</p>
<p>The function's return value should be the number of elements in the returned array.</p>
<p>If <i>pvOutput</i> is <b>NULL</b>, the function should just return the number of array elements required.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PRINTERMEM</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be an integer representing the amount of available printer memory, in kilobytes.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PRINTRATE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be an integer representing the print rate, in the units specified for DC_PRINTRATEUNIT.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PRINTRATEPPM</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be an integer representing the print rate, in pages per minute.</p>
</td>
</tr>
<tr>
<td>
<p>DC_PRINTRATEUNIT</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should identify the units used for specifying the value returned for DC_PRINTRATE. One of the following constants must be specified: </p>
<p>PRINTRATEUNIT_PPM - pages/min.</p>
<p>PRINTRATEUNIT_CPS - chars./sec.</p>
<p>PRINTRATEUNIT_LPM - lines/min.</p>
<p>PRINTRATEUNIT_IPM - inches/min.</p>
</td>
</tr>
<tr>
<td>
<p>DC_SIZE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the <b>dmSize</b> member of the driver's internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>DC_STAPLE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be <b>TRUE</b> if the printer supports stapling, and <b>FALSE</b> if the printer does not support stapling.</p>
</td>
</tr>
<tr>
<td>
<p>DC_TRUETYPE</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value can be zero, one, or more of the following flags:</p>
<p>DCTT_BITMAP: The device can print TrueType fonts as graphics.</p>
<p>DCTT_DOWNLOAD: The device can accept downloaded TrueType fonts.</p>
<p>DCTT_DOWNLOAD_OUTLINE: (Windows 95/98/Me only) The device can download outline TrueType fonts.</p>
<p>DCTT_SUBDEV: The device can substitute device fonts for TrueType fonts.</p>
</td>
</tr>
<tr>
<td>
<p>DC_VERSION</p>
</td>
<td>
<p>The <i>pvOutput</i> parameter is not used.</p>
<p>The function's return value should be the <b>dmSpecVersion</b> member of the driver's internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pvOutput</i> [out]

<dd>
<p>A caller-supplied pointer to a buffer to receive function-supplied information. The buffer's use is dependent on the value received for the <i>iDevCap</i> parameter.</p>
</dd>

### -param <i>pDevMode</i> [in]

<dd>
<p>A caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure that describes the current print job characteristics. If this parameter is <b>NULL</b>, <b>DrvDeviceCapabilities</b> retrieves the current default initialization values for the specified printer driver, such as the user default DEVMODEW structure of the print queue.</p>
</dd>
</dl>

## -returns
<p>The function's return value is dependent on the value received for the <i>iDevCap</i> parameter. If the received <i>iDevCap</i> value represents a capability that the driver does not support, or if an error is encountered, the function should return GDI_ERROR.</p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>