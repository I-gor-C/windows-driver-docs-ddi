---
UID: NC.d3d10umddi.PFND3D10DDI_CHECKCOUNTER
title: PFND3D10DDI_CHECKCOUNTER
author: windows-driver-content
description: The CheckCounter function retrieves information that describes a counter.
old-location: display\checkcounter.htm
old-project: display
ms.assetid: 592a5146-a2fe-41d1-854b-df27a97bd513
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CheckCounter
req.alt-loc: d3d10umddi.h
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
req.iface: 
---

# PFND3D10DDI_CHECKCOUNTER callback



## -description
<p>The <b>CheckCounter</b> function retrieves information that describes a counter. </p>


## -prototype

````
PFND3D10DDI_CHECKCOUNTER CheckCounter;

VOID APIENTRY CheckCounter(
  _In_    D3D10DDI_HDEVICE      hDevice,
  _In_    D3D10DDI_QUERY        Query,
  _Out_   D3D10DDI_COUNTER_TYPE *pCounterType,
  _Out_   UINT                  *pActiveCounters,
  _Out_   LPSTR                 pName,
  _Inout_ UINT                  *pNameLength,
  _Out_   LPSTR                 pUnits,
  _Inout_ UINT                  *pUnitsLength,
  _Out_   LPSTR                 pDescription,
  _Inout_ UINT                  *pDescriptionLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>Query</i> [in]

<dd>
<p> A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541850">D3D10DDI_QUERY</a>-typed value that identifies the counter identifier that information is retrieved for.</p>
</dd>

### -param <i>pCounterType</i> [out]

<dd>
<p>A pointer to a variable that receives one of the following values from the D3D10DDI_COUNTER_TYPE enumeration that identifies the data type that the counter outputs. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3D10DDI_COUNTER_TYPE_FLOAT32</p>
</td>
<td>
<p>Single-precision float</p>
</td>
</tr>
<tr>
<td>
<p>D3D10DDI_COUNTER_TYPE_UINT16</p>
</td>
<td>
<p>16-bit value</p>
</td>
</tr>
<tr>
<td>
<p>D3D10DDI_COUNTER_TYPE_UINT32</p>
</td>
<td>
<p>32-bit value</p>
</td>
</tr>
<tr>
<td>
<p>D3D10DDI_COUNTER_TYPE_UINT64</p>
</td>
<td>
<p>64-bit value</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pActiveCounters</i> [out]

<dd>
<p>A pointer to a variable that receives the number of simultaneously active counters that are allocated for the creation of the counter identifier that <i>Query</i> identifies. </p>
</dd>

### -param <i>pName</i> [out]

<dd>
<p>A pointer that the driver returns a NULL-terminated string to that contains the name of the counter identifier. </p>
</dd>

### -param <i>pNameLength</i> [in, out]

<dd>
<p>A pointer to a variable that receives the size, in bytes, of the NULL-terminated string that the <i>pName</i> parameter specifies.  </p>
</dd>

### -param <i>pUnits</i> [out]

<dd>
<p>A pointer that the driver returns a NULL-terminated string to that contains the name of the units that the counter identifier measures. </p>
</dd>

### -param <i>pUnitsLength</i> [in, out]

<dd>
<p> A pointer to a variable that receives the size, in bytes, of the NULL-terminated string that the <i>pUnits</i> parameter specifies. </p>
</dd>

### -param <i>pDescription</i> [out]

<dd>
<p>A pointer that the driver returns a NULL-terminated string to that contains the description of what the counter identifier measures. </p>
</dd>

### -param <i>pDescriptionLength</i> [in, out]

<dd>
<p> A pointer to a variable that receives the size, in bytes, of the NULL-terminated string that the <i>pDescription</i> parameter specifies. </p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The driver's <b>CheckCounter</b> function can call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set the ERR_UNSUPPORTED error code if the <i>Query</i> parameter of <b>CheckCounter</b>specifies a well-known counter that the device does not support.</p>

<p>The driver must validate a device-dependent counter identifier to ensure the identifier is within range. The driver must also ensure that enough space exists to copy each counter string into each buffer that the Microsoft Direct3D runtime provides. The driver can call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set the E_INVALIDARG error code if there is not enough space for any of the provided buffers.</p>

<p>The driver's <b>CheckCounter</b> function cannot call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set the D3DDDIERR_DEVICEREMOVED error code because <b>CheckCounter</b> is a capability-check type of function. The driver must ensure that it has enough information after device creation to respond to a call to <b>CheckCounter</b>, even in the presence of D3DDDIERR_DEVICEREMOVED. </p>

<p>The driver's <b>CheckCounter</b> function can call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set the ERR_UNSUPPORTED error code if the <i>Query</i> parameter of <b>CheckCounter</b>specifies a well-known counter that the device does not support.</p>

<p>The driver must validate a device-dependent counter identifier to ensure the identifier is within range. The driver must also ensure that enough space exists to copy each counter string into each buffer that the Microsoft Direct3D runtime provides. The driver can call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set the E_INVALIDARG error code if there is not enough space for any of the provided buffers.</p>

<p>The driver's <b>CheckCounter</b> function cannot call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set the D3DDDIERR_DEVICEREMOVED error code because <b>CheckCounter</b> is a capability-check type of function. The driver must ensure that it has enough information after device creation to respond to a call to <b>CheckCounter</b>, even in the presence of D3DDDIERR_DEVICEREMOVED. </p>

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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541850">D3D10DDI_QUERY</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CHECKCOUNTER callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
