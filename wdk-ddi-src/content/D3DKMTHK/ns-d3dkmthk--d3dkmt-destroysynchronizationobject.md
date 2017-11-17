---
UID: NS.d3dkmthk._D3DKMT_DESTROYSYNCHRONIZATIONOBJECT
title: D3DKMT_DESTROYSYNCHRONIZATIONOBJECT
author: windows-driver-content
description: The D3DKMT_DESTROYSYNCHRONIZATIONOBJECT structure contains the handle to a synchronization object to destroy.
old-location: display\d3dkmt_destroysynchronizationobject.htm
ms.assetid: d6be16da-7f92-4c10-af8b-7ecd05ef6856
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DESTROYSYNCHRONIZATIONOBJECT
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
ms.keywords: D3DKMT_DESTROYSYNCHRONIZATIONOBJECT, D3DKMT_DESTROYSYNCHRONIZATIONOBJECT
req.iface: 
---

# D3DKMT_DESTROYSYNCHRONIZATIONOBJECT structure



## -description
<p>The D3DKMT_DESTROYSYNCHRONIZATIONOBJECT structure contains the handle to a synchronization object to destroy.</p>


## -syntax

````
typedef struct _D3DKMT_DESTROYSYNCHRONIZATIONOBJECT {
  D3DKMT_HANDLE hSyncObject;
} D3DKMT_DESTROYSYNCHRONIZATIONOBJECT;
````


## -struct-fields
<dl>

### -field <b>hSyncObject</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546869">D3DKMTCreateSynchronizationObject</a> function returns and that identifies the kernel-mode synchronization object to destroy. </p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546869">D3DKMTCreateSynchronizationObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546935">D3DKMTDestroySynchronizationObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_DESTROYSYNCHRONIZATIONOBJECT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
