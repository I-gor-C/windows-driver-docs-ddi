---
UID: NS.iscsiop._ScsiReportLuns_IN
title: ScsiReportLuns_IN
author: windows-driver-content
description: The ScsiReportLuns_IN structure holds the input data for the ScsiReportLuns method.
old-location: storage\scsireportluns_in.htm
old-project: storage
ms.assetid: ba1d67f7-cb90-473a-849d-7990889e4a40
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiReportLuns_IN, ScsiReportLuns_IN, *PScsiReportLuns_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiReportLuns_IN
req.alt-loc: iscsiop.h
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

# ScsiReportLuns_IN structure



## -description
<p>The ScsiReportLuns_IN structure holds the input data for the <a href="storage.scsireportluns">ScsiReportLuns</a> method.</p>


## -syntax

````
typedef struct _ScsiReportLuns_IN {
  ULONGLONG UniqueSessionId;
} ScsiReportLuns_IN, *PScsiReportLuns_IN;
````


## -struct-fields
<dl>

### -field <b>UniqueSessionId</b>

<dd>
<p>A 64-bit integer that uniquely identifies the session. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in their <i>UniqueSessionId</i> parameter. </p>
</dd>
</dl>

## -remarks
<p>You must implement this method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.addconnectiontosession">AddConnectionToSession</a>
</dt>
<dt>
<a href="storage.logintotarget">LoginToTarget</a>
</dt>
<dt>
<a href="storage.scsireportluns">ScsiReportLuns</a>
</dt>
<dt>
<a href="..\hbapiwmi\ns-hbapiwmi--scsireportluns-out.md">ScsiReportLuns_OUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiReportLuns_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
