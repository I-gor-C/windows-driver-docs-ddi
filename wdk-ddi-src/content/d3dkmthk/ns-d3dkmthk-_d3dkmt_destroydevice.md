---
UID: NS.D3DKMTHK._D3DKMT_DESTROYDEVICE
title: _D3DKMT_DESTROYDEVICE
author: windows-driver-content
description: The D3DKMT_DESTROYDEVICE structure contains a handle to the kernel-mode device context to release.
old-location: display\d3dkmt_destroydevice.htm
old-project: display
ms.assetid: f74ea9da-71ba-466a-b102-78d999d38096
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_DESTROYDEVICE, D3DKMT_DESTROYDEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DESTROYDEVICE
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
---

# _D3DKMT_DESTROYDEVICE structure



## -description
The D3DKMT_DESTROYDEVICE structure contains a handle to the kernel-mode device context to release.


## -syntax

````
typedef struct _D3DKMT_DESTROYDEVICE {
  D3DKMT_HANDLE hDevice;
} D3DKMT_DESTROYDEVICE;
````


## -struct-fields

### -field hDevice

[in] A handle to the device context that the Microsoft DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) supplied and that is returned from the call to the <a href="display.d3dkmtcreatedevice">D3DKMTCreateDevice</a> function.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="display.d3dkmtcreatedevice">D3DKMTCreateDevice</a>
</dt>
<dt>
<a href="display.d3dkmtdestroydevice">D3DKMTDestroyDevice</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_DESTROYDEVICE structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
