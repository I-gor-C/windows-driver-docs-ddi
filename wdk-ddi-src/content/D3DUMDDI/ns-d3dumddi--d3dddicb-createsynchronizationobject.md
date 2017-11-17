---
UID: NS.d3dumddi._D3DDDICB_CREATESYNCHRONIZATIONOBJECT
title: D3DDDICB_CREATESYNCHRONIZATIONOBJECT
author: windows-driver-content
description: The D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure describes a synchronization object that the pfnCreateSynchronizationObjectCb function creates.
old-location: display\d3dddicb_createsynchronizationobject.htm
ms.assetid: e799a11c-eab7-4d85-9ed8-063e87aa351f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_CREATESYNCHRONIZATIONOBJECT
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDICB_CREATESYNCHRONIZATIONOBJECT, D3DDDICB_CREATESYNCHRONIZATIONOBJECT
req.iface: 
---

# D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure



## -description
<p>The D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure describes a synchronization object that the <a href="https://msdn.microsoft.com/1b87d3cc-685a-4768-b4fd-dbe0a0cbec37">pfnCreateSynchronizationObjectCb</a> function creates.</p>


## -syntax

````
typedef struct _D3DDDICB_CREATESYNCHRONIZATIONOBJECT {
  D3DDDI_SYNCHRONIZATIONOBJECTINFO Info;
  D3DKMT_HANDLE                    hSyncObject;
} D3DDDICB_CREATESYNCHRONIZATIONOBJECT;
````


## -struct-fields
<dl>

### -field <b>Info</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544657">D3DDDI_SYNCHRONIZATIONOBJECTINFO</a> structure that contains information about the kernel-mode synchronization object.</p>
</dd>

### -field <b>hSyncObject</b>

<dd>
<p>[out] A <b>D3DKMT_HANDLE</b> value that represents a kernel-mode handle to the kernel-mode synchronization object. </p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544657">D3DDDI_SYNCHRONIZATIONOBJECTINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1b87d3cc-685a-4768-b4fd-dbe0a0cbec37">pfnCreateSynchronizationObjectCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_CREATESYNCHRONIZATIONOBJECT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
