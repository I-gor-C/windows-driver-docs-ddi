---
UID: NS.61883._SET_FCP_NOTIFY
title: SET_FCP_NOTIFY
author: windows-driver-content
description: This structure is used for FCP notification.
old-location: ieee\set_fcp_notify.htm
ms.assetid: 94A966C4-9FFA-4937-B7D8-D1A3608E4A7F
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SET_FCP_NOTIFY
req.alt-loc: 61883.h
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
ms.keywords: SET_FCP_NOTIFY, SET_FCP_NOTIFY, *PSET_FCP_NOTIFY
---

# SET_FCP_NOTIFY structure



## -description
<p>This structure is used for FCP notification. </p>


## -syntax

````
typedef struct _SET_FCP_NOTIFY {
  ULONG        Flags;
  NODE_ADDRESS NodeAddress;
} SET_FCP_NOTIFY, *PSET_FCP_NOTIFY;
````


## -struct-fields
<dl>

### -field <b><b>Flags</b></b>

<dd>
<p>Specifies the notification requested by the driver. The driver can register by setting <b>Flags</b> with either or both of the following: </p>
<dl>
<dd>
<p>REGISTER_FCP_RESPONSE_NOTIFY</p>
</dd>
<dd>
<p>REGISTER_FCP_REQUEST_NOTIFY </p>
</dd>
</dl>
<p>The driver can cancel notification by setting <b>Flags</b> with DEREGISTER_FCP_NOTIFY, which clears REGISTER_FCP_RESPONSE_NOTIFY and REGISTER_FCP_REQUEST_NOTIFY.</p>
</dd>

### -field <b><b>NodeAddress</b></b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20SET_FCP_NOTIFY structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
