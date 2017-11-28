---
UID: NS.d3dkmthk._D3DKMT_QUERYADAPTERINFO
title: D3DKMT_QUERYADAPTERINFO
author: windows-driver-content
description: The D3DKMT_QUERYADAPTERINFO structure contains information that describes the graphics adapter.
old-location: display\d3dkmt_queryadapterinfo.htm
old-project: display
ms.assetid: 2bc9afc3-2fcf-4f62-85d4-67f824733904
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_QUERYADAPTERINFO, D3DKMT_QUERYADAPTERINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Supported  starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_QUERYADAPTERINFO
req.alt-loc: d3dkmthk.h
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

# D3DKMT_QUERYADAPTERINFO structure



## -description
<p>The D3DKMT_QUERYADAPTERINFO structure contains information that describes the graphics adapter.</p>


## -syntax

````
typedef struct _D3DKMT_QUERYADAPTERINFO {
  D3DKMT_HANDLE           hAdapter;
  KMTQUERYADAPTERINFOTYPE Type;
  VOID                    *pPrivateDriverData;
  UINT                    PrivateDriverDataSize;
} D3DKMT_QUERYADAPTERINFO;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd>
<p>[in] A handle to the graphics adapter that information is retrieved about.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>[in] A value of type KMTQUERYADAPTERINFOTYPE that indicates the type of information to retrieve. The following table lists the possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KMTQAITYPE_UMDRIVERPRIVATE</p>
</td>
<td>
<p>The buffer that <b>pPrivateDriverData</b> points to is populated with private driver data in a vendor-specific format. To read and process the private data, a tight coupling between the OpenGL installable client driver (ICD) and the display miniport driver must exist.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_UMDRIVERNAME</p>
</td>
<td>
<p>The <b>pPrivateDriverData</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548384">D3DKMT_UMDFILENAMEINFO</a> structure that is filled with the name of the OpenGL ICD that depends on the particular version of DirectX. Non-DirectX applications can use this name to call the OpenGL ICD directly, although such usage is not recommended.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_UMOPENGLINFO</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548123">D3DKMT_OPENGLINFO</a> structure that contains information about the OpenGL ICD.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_GETSEGMENTSIZE</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548256">D3DKMT_SEGMENTSIZEINFO</a> structure that contains information about the size of memory and aperture segments.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_ADAPTERGUID</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a variable that contains the GUID for the graphics adapter.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_FLIPQUEUEINFO</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548010">D3DKMT_FLIPQUEUEINFO</a> structure that contains information about the queue of flip operations.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_ADAPTERADDRESS</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547280">D3DKMT_ADAPTERADDRESS</a> structure that contains information about the physical location of the graphics adapter.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_SETWORKINGSETINFO</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548457">D3DKMT_WORKINGSETINFO</a> structure that contains information about the working set.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_ADAPTERREGISTRYINFO</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547286">D3DKMT_ADAPTERREGISTRYINFO</a> structure that contains registry information about the graphics adapter.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_CURRENTDISPLAYMODE</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547860">D3DKMT_CURRENTDISPLAYMODE</a> structure that contains the current display mode.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_MODELIST</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a> structures for the list of display modes.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_CHECKDRIVERUPDATESTATUS</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to the driver update status.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_VIRTUALADDRESSINFO </p>
</td>
<td>
<p>Reserved for future use.</p>
<p>Supported starting with  Windows 7.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_DRIVERVERSION</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a variable that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547964">D3DKMT_DRIVERVERSION</a>-typed value that indicates the version of the display driver model that the display miniport driver supports.</p>
<p>Supported starting with  Windows 7.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_ADAPTERTYPE</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439472">D3DKMT_ADAPTERTYPE</a> structure that specifies the  graphics adapter type.</p>
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_OUTPUTDUPLCONTEXTSCOUNT</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406505">D3DKMT_OUTPUTDUPLCONTEXTSCOUNT</a> structure that specifies the  number of current <a href="direct3ddxgi.desktop_dup_api">Desktop Duplication API</a> (DDA) clients that are attached to a given video present network (VidPN).</p>
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_WDDM_1_2_CAPS</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406678">D3DKMT_WDDM_1_2_CAPS</a> structure that specifies the  WDDM 1.2 and later capabilities of the graphics adapter and display miniport driver.</p>
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_UMD_DRIVER_VERSION</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406598">D3DKMT_UMD_DRIVER_VERSION</a> structure that specifies the  user-mode driver version.</p>
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_DIRECTFLIP_SUPPORT</p>
</td>
<td>
<p><b>pPrivateDriverData</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406459">D3DKMT_DIRECTFLIP_SUPPORT</a> structure that specifies whether the user-mode driver supports Direct Flip operations.</p>
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_MULTIPLANEOVERLAY_SUPPORT</p>
</td>
<td>
<p>Reserved for future use.</p>
<p>Supported starting with  Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_DLIST_DRIVER_NAME</p>
</td>
<td>
<p>Reserved for future use.</p>
<p>Supported starting with  Windows 8.1.</p>
</td>
</tr>
<tr>
<td>
<p>KMTQAITYPE_WDDM_1_3_CAPS</p>
</td>
<td>
<p>Reserved for future use.</p>
<p>Supported starting with  Windows 8.1.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[out] A pointer to a buffer that the display miniport driver can fill with the requested information.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in/out] The size, in bytes, of the buffer that <b>pPrivateDriverData</b> points to.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported  starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547280">D3DKMT_ADAPTERADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547286">D3DKMT_ADAPTERREGISTRYINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439472">D3DKMT_ADAPTERTYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547860">D3DKMT_CURRENTDISPLAYMODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406459">D3DKMT_DIRECTFLIP_SUPPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547964">D3DKMT_DRIVERVERSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548010">D3DKMT_FLIPQUEUEINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548123">D3DKMT_OPENGLINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406505">D3DKMT_OUTPUTDUPLCONTEXTSCOUNT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548256">D3DKMT_SEGMENTSIZEINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406598">D3DKMT_UMD_DRIVER_VERSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548384">D3DKMT_UMDFILENAMEINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406678">D3DKMT_WDDM_1_2_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548457">D3DKMT_WORKINGSETINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547100">D3DKMTQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_QUERYADAPTERINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
