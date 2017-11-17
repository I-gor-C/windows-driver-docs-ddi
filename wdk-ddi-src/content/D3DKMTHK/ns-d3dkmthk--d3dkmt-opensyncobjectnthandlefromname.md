---
UID: NS.d3dkmthk._D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
title: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
author: windows-driver-content
description: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME is used with D3DKMTOpenSyncObjectNtHandleFromName to open an NT handle for a named shared monitored fence object.
old-location: display\d3dkmt_opensyncobjectnthandlefromname.htm
ms.assetid: 6435D3B7-A1B7-4417-8272-C505A5FA500E
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME, D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME
req.iface: 
---

# D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME structure



## -description
<p><b>D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906779">D3DKMTOpenSyncObjectNtHandleFromName</a> to open an NT handle for a named shared monitored fence object.</p>


## -syntax

````
typedef struct _D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME {
  DWORD             dwDesiredAccess;
  OBJECT_ATTRIBUTES *pObjAttrib;
  HANDLE            hNtHandle;
} D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME;
````


## -struct-fields
<dl>

### -field <b>dwDesiredAccess</b>

<dd>
<p>[in] Access attributes for opening a shared monitored fence sync object, such as <b>D3DDDI_SYNC_OBJECT_WAIT</b>, <b>D3DDDI_SYNC_OBJECT_SIGNAL</b>, or <b>D3DDDI_SYNC_OBJECT_ALL_ACCESS</b>.</p>
</dd>

### -field <b>pObjAttrib</b>

<dd>
<p>[in] Object attributes for opening the object handle, including the shared object name information.</p>
</dd>

### -field <b>hNtHandle</b>

<dd>
<p>[out] NT handle to the sync object that can be used to open it via <a href="https://msdn.microsoft.com/library/windows/hardware/dn906778">D3DKMTOpenSyncObjectFromNtHandle2</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906779">D3DKMTOpenSyncObjectNtHandleFromName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906778">D3DKMTOpenSyncObjectFromNtHandle2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_OPENSYNCOBJECTNTHANDLEFROMNAME structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
