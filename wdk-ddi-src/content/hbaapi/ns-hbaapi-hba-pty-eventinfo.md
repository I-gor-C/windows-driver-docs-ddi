---
UID: NS.hbaapi.HBA_Pty_EventInfo
title: HBA_Pty_EventInfo
author: windows-driver-content
description: The HBA_Link_EventInfo structure contains information about a WMI proprietary event associated with the fibre channel HBA API.
old-location: storage\hba_pty_eventinfo.htm
old-project: storage
ms.assetid: 4291e6cd-9497-4106-82bf-c054108a0946
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_Pty_EventInfo, HBA_PTY_EVENTINFO, *PHBA_PTY_EVENTINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_PTY_EVENTINFO
req.alt-loc: hbaapi.h
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

# HBA_Pty_EventInfo structure



## -description
<p>The HBA_Link_EventInfo structure contains information about a WMI proprietary event associated with the fibre channel HBA API. </p>


## -syntax

````
typedef struct HBA_Pty_EventInfo {
  HBA_UINT32 PtyData[4];
} HBA_PTY_EVENTINFO, *PHBA_PTY_EVENTINFO;
````


## -struct-fields
<dl>

### -field <b>PtyData</b>

<dd>
<p>Contains proprietary data defined by the vendor. </p>
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
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-eventinfo.md">HBA_EventInfo</a>
</dt>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-link-eventinfo.md">HBA_Link_EventInfo</a>
</dt>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-rscn-eventinfo.md">HBA_RSCN_EventInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_Pty_EventInfo structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
