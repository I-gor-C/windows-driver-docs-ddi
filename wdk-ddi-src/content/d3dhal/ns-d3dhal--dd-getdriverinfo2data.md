---
UID: NS.d3dhal._DD_GETDRIVERINFO2DATA
title: DD_GETDRIVERINFO2DATA
author: windows-driver-content
description: DirectX 8.0 and later versions only. DD_GETDRIVERINFO2DATA is passed in the lpvData member of the DD_GETDRIVERINFODATA structure when GUID_GetDriverInfo2 is specified in the guidInfo member of DD_GETDRIVERINFODATA in a DdGetDriverInfo call.
old-location: display\dd_getdriverinfo2data.htm
ms.assetid: f1b3e432-6972-49ff-9fce-b642c1be17ea
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DD_GETDRIVERINFO2DATA
req.alt-loc: d3dhal.h
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
ms.keywords: DD_GETDRIVERINFO2DATA, DD_GETDRIVERINFO2DATA
req.iface: 
---

# DD_GETDRIVERINFO2DATA structure



## -description
<p>
   DirectX 8.0 and later versions only.
   </p>
<p>DD_GETDRIVERINFO2DATA is passed in the <b>lpvData</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551550">DD_GETDRIVERINFODATA</a> structure when GUID_GetDriverInfo2 is specified in the <b>guidInfo</b> member of DD_GETDRIVERINFODATA in a <a href="https://msdn.microsoft.com/89a22163-a678-4c72-932a-ae4d17922e0b">DdGetDriverInfo</a> call.</p>


## -syntax

````
typedef struct _DD_GETDRIVERINFO2DATA {
  DWORD dwReserved;
  DWORD dwMagic;
  DWORD dwType;
  DWORD dwExpectedSize;
} DD_GETDRIVERINFO2DATA;
````


## -struct-fields
<dl>

### -field <b>dwReserved</b>

<dd>
<p>Specifies a reserved field. Driver should not read or write.</p>
</dd>

### -field <b>dwMagic</b>

<dd>
<p>Specifies the magic number. Has the value 
	  D3DGDI2_MAGIC if this is a 
	  <a href="https://msdn.microsoft.com/5e2dd363-9e72-4674-940e-8b4f06f6eb14">GetDriverInfo2</a> 
	  call. Otherwise this structure is, in fact, a 
	  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551716">DD_STEREOMODE</a> 
	  call.</p>
</dd>

### -field <b>dwType</b>

<dd>
<p>Specifies the type of information requested, which can contain one of the following D3DGDI2_TYPE_<i>Xxx</i> 
	values. Driver should only read (not write) this member.
	</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>D3DGDI2_TYPE_DEFER_AGP_FREES</td>
<td>
<p><b>NT-based operating systems only.</b></p>
<p>Is used to notify the driver that it should properly 
		handle the destruction of <a href="https://msdn.microsoft.com/05a2f942-4374-421e-8292-d122f9fe3571">AGP memory</a> for surfaces. 
		The runtime provides a pointer to a 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551528">DD_FREE_DEFERRED_AGP_DATA</a> 
		structure in the <b>lpvData</b> field of the DD_GETDRIVERINFODATA data structure.</p>
<p>The driver sometimes receives this notification before a display mode change occurs. The runtime 
		only sends this notification if it is to be used to perform the display mode change. Drivers should check 
		the process identifier (PID) of the process destroying the surface against the process that created the 
		surface. If the PIDs are different, the driver probably should not destroy the user-mode mappings of the 
		AGP memory because an application might still be using the memory.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_DEFERRED_AGP_AWARE</td>
<td>
<p><b>NT-based operating systems only.</b></p>
<p>Is used to inform the driver that the runtime sends 
		D3DGDI2_TYPE_FREE_DEFERRED_AGP and D3DGDI2_TYPE_DEFER_AGP_FREES notifications at the appropriate time 
		(such as, after the last outstanding <a href="https://msdn.microsoft.com/05a2f942-4374-421e-8292-d122f9fe3571">AGP memory</a> 
		lock is released). The runtime provides a pointer to a 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff550562">DD_DEFERRED_AGP_AWARE_DATA</a> 
		structure in the 
		<b>lpvData</b> field 
		of the DD_GETDRIVERINFODATA data structure.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_DXVERSION</td>
<td>
<p>Is used to notify the driver of the current DX runtime version 
		being used by the application. The runtime provides a pointer to a 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551515">DD_DXVERSION</a> structure in the <b>lpvData</b> 
		field of the DD_GETDRIVERINFODATA data structure.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_FREE_DEFERRED_AGP</td>
<td>
<p><b>NT-based operating systems only.</b></p>
<p>Is used to notify the driver that it is now safe 
		to destroy all the user-mode mappings of the 
		<a href="https://msdn.microsoft.com/05a2f942-4374-421e-8292-d122f9fe3571">AGP memory</a>. The driver preserved these user-mode 
		mappings when surfaces were destroyed and it received a D3DGDI2_TYPE_DEFER_AGP_FREES notification. The 
		runtime provides a pointer to a 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551528">DD_FREE_DEFERRED_AGP_DATA</a> 
		structure in the <b>lpvData</b> field of the DD_GETDRIVERINFODATA data structure.</p>
<p>The driver receives 
		this notification when all display devices within the process stop using surfaces, textures, vertex 
		buffers, and index buffers that were locked at the time of the display mode change. </p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETADAPTERGROUP</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used to query the driver for the identity of 
		the group of adapters that are part of its 
		multiple-head video card. This group shares video 
		hardware 
		like video memory and the 3D accelerator. The 
		driver should set the data structure pointed to by 
		the <b>lpvData</b> field of the 
		DD_GETDRIVERINFODATA data structure to 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551529">DD_GETADAPTERGROUPDATA</a>.
		</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETD3DCAPS8</td>
<td>
<p>This type indicates that the runtime requests to receive a 
		D3DCAPS8 structure giving the DirectX 8.0 style capabilities of the device. The driver should copy an 
		initialized D3DCAPS8 structure into the <b>lpvData</b> field of the DD_GETDRIVERINFODATA structure.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETD3DCAPS9</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p><b>Required for DirectX 9.0 and later drivers.</b></p>
<p>This type indicates that the runtime requests to 
		receive a D3DCAPS9 structure giving the 
		DirectX 9.0 style capabilities of the device. The 
		driver should copy an initialized D3DCAPS9 
		structure 
		into the <b>lpvData</b> field 
		of the DD_GETDRIVERINFODATA structure.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETD3DQUERY</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used to query 
		the driver for information about a particular query 
		type that it supports. The driver should set the 
		data 
		structure pointed to by the 
		<b>lpvData</b> 
		field of 
		the DD_GETDRIVERINFODATA data structure to 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551541">DD_GETD3DQUERYDATA</a>.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETD3DQUERYCOUNT</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used to 
		query the driver for the number of query types that it 
		supports. The driver should set the data structure 
		pointed to by the <b>lpvData</b> field of the 
		DD_GETDRIVERINFODATA data structure to 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551539">DD_GETD3DQUERYCOUNTDATA</a>.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETDDIVERSION</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used to 
		query the driver for the version of the DDI that 
		the driver supports; this DDI version, in turn, 
		depends 
		on the version of DirectX that makes this request. 
		The driver should set the <b>dwDDIVersion</b> 
		member 
		of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551545">DD_GETDDIVERSIONDATA</a> 
		structure, 
		which the <b>lpvData</b> field of the 
		DD_GETDRIVERINFODATA data structure points to, to 
		the appropriate 
		DDI version.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETEXTENDEDMODE</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used to 
		query the driver for information about a particular 
		extended display mode that it supports. The driver 
		should set the data structure pointed to by the 
		<b>lpvData</b> field of the DD_GETDRIVERINFODATA 
		data 
		structure to 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551559">DD_GETEXTENDEDMODEDATA</a>.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETEXTENDEDMODECOUNT</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used 
		to query the driver for the number of extended 
		display modes that it supports. The driver should 
		set the 
		data structure pointed to by the <b>lpvData</b> 
		field of the DD_GETDRIVERINFODATA data structure to 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551558">DD_GETEXTENDEDMODECOUNTDATA</a>.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETFORMAT</td>
<td>
<p>Is used to query for a particular surface format from the driver. 
		The data structure pointed to by the <b>lpvData</b> 
		field of the DD_GETDRIVERINFODATA data structure is 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551569">DD_GETFORMATDATA</a>.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETFORMATCOUNT</td>
<td>
<p>Is used to request the number of DirectX 8.0 and
		later style surface formats supported by the 
		driver. The data structure pointed to by the 
		<b>lpvData</b> 
		field of the DD_GETDRIVERINFODATA is 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551566">DD_GETFORMATCOUNTDATA</a>.</p>
</td>
</tr>
<tr>
<td>D3DGDI2_TYPE_GETMULTISAMPLEQUALITYLEVELS</td>
<td>
<p><b>DirectX 9.0 and later versions only.</b></p>
<p>Is used to query the driver for the number of 
		multiple-sample quality levels for a given 
		render-target format that it supports. Whether the 
		display device supports maskable or submaskable 
		multisampling, the driver for the device must provide 
		the number of quality levels for the 
		D3DMULTISAMPLE_NONMASKABLE multiple-sample type. The 
		driver should set the data structure pointed to by 
		the <b>lpvData</b> 
		field of the DD_GETDRIVERINFODATA 
		data structure to 
		<a href="https://msdn.microsoft.com/library/windows/hardware/ff551665">DD_MULTISAMPLEQUALITYLEVELSDATA</a>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwExpectedSize</b>

<dd>
<p>Specifies the expected size, in bytes, of the information requested. Driver should only read (not write) this member.</p>
</dd>
</dl>

## -remarks
<p>The <b>dwExpectedSize</b> member of the DD_GETDRIVERINFODATA structure is not used when a <a href="https://msdn.microsoft.com/5e2dd363-9e72-4674-940e-8b4f06f6eb14">GetDriverInfo2</a> request is being made. Its value is undefined in this case and should be ignored. Instead, the actual expected size of the data is found in the <b>dwExpectedSize</b> member of DD_GETDRIVERINFO2DATA.</p>

<p>The following code fragment demonstrates how to handle <a href="https://msdn.microsoft.com/5e2dd363-9e72-4674-940e-8b4f06f6eb14">GetDriverInfo2</a>:</p>

<p>For more information about D3DCAPS8 and D3DCAPS9, see the DirectX SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550562">DD_DEFERRED_AGP_AWARE_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551515">DD_DXVERSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551528">DD_FREE_DEFERRED_AGP_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551529">DD_GETADAPTERGROUPDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551539">DD_GETD3DQUERYCOUNTDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551541">DD_GETD3DQUERYDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551545">DD_GETDDIVERSIONDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/89a22163-a678-4c72-932a-ae4d17922e0b">DdGetDriverInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551550">DD_GETDRIVERINFODATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551558">DD_GETEXTENDEDMODECOUNTDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551559">DD_GETEXTENDEDMODEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551566">DD_GETFORMATCOUNTDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551569">DD_GETFORMATDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551665">DD_MULTISAMPLEQUALITYLEVELSDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551716">DD_STEREOMODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DD_GETDRIVERINFO2DATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
