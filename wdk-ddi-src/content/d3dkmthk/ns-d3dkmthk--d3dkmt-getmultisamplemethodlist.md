---
UID: NS.d3dkmthk._D3DKMT_GETMULTISAMPLEMETHODLIST
title: D3DKMT_GETMULTISAMPLEMETHODLIST
author: windows-driver-content
description: The D3DKMT_GETMULTISAMPLEMETHODLIST structure describes parameters to retrieve the list of multiple-sample methods for an allocation.
old-location: display\d3dkmt_getmultisamplemethodlist.htm
old-project: display
ms.assetid: 138f6f75-3986-42f8-840c-d48edb271203
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_GETMULTISAMPLEMETHODLIST, D3DKMT_GETMULTISAMPLEMETHODLIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_GETMULTISAMPLEMETHODLIST
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

# D3DKMT_GETMULTISAMPLEMETHODLIST structure



## -description
<p>The D3DKMT_GETMULTISAMPLEMETHODLIST structure describes parameters to retrieve the list of multiple-sample methods for an allocation.</p>


## -syntax

````
typedef struct _D3DKMT_GETMULTISAMPLEMETHODLIST {
  D3DKMT_HANDLE                  hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           Width;
  UINT                           Height;
  D3DDDIFORMAT                   Format;
  D3DKMT_MULTISAMPLEMETHOD       *pMethodList;
  UINT                           MethodCount;
} D3DKMT_GETMULTISAMPLEMETHODLIST;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd>
<p>[in] A handle to the graphics adapter.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology that the allocation is on. </p>
</dd>

### -field <b>Width</b>

<dd>
<p>[in] The width of the allocation, in pixels.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>[in] The height of the allocation, in pixels.</p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the allocation.</p>
</dd>

### -field <b>pMethodList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548098">D3DKMT_MULTISAMPLEMETHOD</a> structures that describe the list of multiple-sampling methods used for the allocation; otherwise, this member is <b>NULL</b>.</p>
</dd>

### -field <b>MethodCount</b>

<dd>
<p>[in/out] On input, the number of elements that the array that is specified by <b>pMethodList</b> can hold. On output, this member specifies the required number of elements that the array that is specified by <b>pMethodList</b> should hold. </p>
</dd>
</dl>

## -remarks
<p>If the runtime returns a non-<b>NULL</b> value in <b>pMethodList</b>, the runtime returns a value in <b>MethodCount</b> that represents the number of elements that the array can hold. If the runtime returns <b>NULL</b> in <b>pMethodList</b>, the runtime returns a value in <b>MethodCount</b> that represents the size of the array buffer that is required, in number of elements. </p>

## -requirements
<table>
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
<dt>D3dkmthk.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548098">D3DKMT_MULTISAMPLEMETHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546975">D3DKMTGetMultisampleMethodList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_GETMULTISAMPLEMETHODLIST structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
