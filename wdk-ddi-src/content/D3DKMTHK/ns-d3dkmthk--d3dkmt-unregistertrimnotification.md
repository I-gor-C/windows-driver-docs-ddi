---
UID: NS.d3dkmthk._D3DKMT_UNREGISTERTRIMNOTIFICATION
title: D3DKMT_UNREGISTERTRIMNOTIFICATION
author: windows-driver-content
description: D3DKMT_UNREGISTERTRIMNOTIFICATION is used with D3DKMTUnregisterTrimNotification to remove a callback registration for a kernel mode device receiving notifications from a graphics framework (such as OpenGL).
old-location: display\d3dkmt_unregistertrimnotification.htm
ms.assetid: 336C5C6A-619B-4D28-9F06-A09CABF78073
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
req.alt-api: D3DKMT_UNREGISTERTRIMNOTIFICATION
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
ms.keywords: D3DKMT_UNREGISTERTRIMNOTIFICATION, D3DKMT_UNREGISTERTRIMNOTIFICATION
req.iface: 
---

# D3DKMT_UNREGISTERTRIMNOTIFICATION structure



## -description
<p><b>D3DKMT_UNREGISTERTRIMNOTIFICATION</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906787">D3DKMTUnregisterTrimNotification</a> to remove a callback registration for a kernel mode device receiving notifications from a graphics framework (such as OpenGL).

</p>


## -syntax

````
typedef struct _D3DKMT_UNREGISTERTRIMNOTIFICATION {
  VOID *Handle;
} D3DKMT_UNREGISTERTRIMNOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>Handle</b>

<dd>
<p>[out] The callback notification handle received from the call to <a href="https://msdn.microsoft.com/library/windows/hardware/dn906781">D3DKMTRegisterTrimNotification</a>.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906787">D3DKMTUnregisterTrimNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906781">D3DKMTRegisterTrimNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_UNREGISTERTRIMNOTIFICATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
