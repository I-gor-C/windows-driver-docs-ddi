---
UID: NE.nfccx._NFC_CX_HOST_ACTION
title: NFC_CX_HOST_ACTION
author: windows-driver-content
description: The NFC_CX_HOST_ACTION enumeration specifies host actions.
old-location: nfpdrivers\nfc_cx_host_action.htm
old-project: nfpdrivers
ms.assetid: CE485A6F-8480-4535-9145-A8CBF78C804D
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: NPI_REGISTRATION_INSTANCE, NPI_REGISTRATION_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfccx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NFC_CX_HOST_ACTION
req.alt-loc: nfccx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Requires same
req.iface: 
---

# NFC_CX_HOST_ACTION enumeration



## -description
<p>The NFC_CX_HOST_ACTION enumeration specifies host actions.</p>


## -syntax

````
typedef enum _NFC_CX_HOST_ACTION { 
  HostActionStart    = 0,
  HostActionStop     = 1,
  HostActionRestart  = 2,
  HostActionUnload   = 3
} NFC_CX_HOST_ACTION;
````


## -enum-fields
<dl>

### -field <a id="HostActionStart"></a><a id="hostactionstart"></a><a id="HOSTACTIONSTART"></a><b>HostActionStart</b>

<dd>
<p>Specifies full initialization.</p>
</dd>

### -field <a id="HostActionStop"></a><a id="hostactionstop"></a><a id="HOSTACTIONSTOP"></a><b>HostActionStop</b>

<dd>
<p>Specifies de-initialization.</p>
</dd>

### -field <a id="HostActionRestart"></a><a id="hostactionrestart"></a><a id="HOSTACTIONRESTART"></a><b>HostActionRestart</b>

<dd>
<p>Specifies a full driver restart.</p>
</dd>

### -field <a id="HostActionUnload"></a><a id="hostactionunload"></a><a id="HOSTACTIONUNLOAD"></a><b>HostActionUnload</b>

<dd>
<p>Specifies to unload the driver.</p>
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
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfccx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a></dt>
<dt><a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [nfpdrivers\nfpdrivers]:%20NFC_CX_HOST_ACTION enumeration%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
