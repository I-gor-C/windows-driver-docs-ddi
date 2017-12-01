---
UID: NS.iscsimgt._ISCSI_Path
title: ISCSI_Path
author: windows-driver-content
description: The ISCSI_Path structure contains information about a connection of the iSCSI portal.
old-location: storage\iscsi_path.htm
old-project: storage
ms.assetid: eebc3e2e-41fe-4087-8916-7c8a71929913
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_Path, ISCSI_Path, *PISCSI_Path
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsimgt.h
req.include-header: Iscsimgt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_Path
req.alt-loc: iscsimgt.h
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

# ISCSI_Path structure



## -description
<p>The ISCSI_Path structure contains information about a connection of the iSCSI portal.</p>


## -syntax

````
typedef struct _ISCSI_Path {
  ULONGLONG UniqueConnectionId;
  ULONGLONG EstimatedLinkSpeed;
  ULONG     PathWeight;
  ULONG     PrimaryPath;
  ULONG     ConnectionStatus;
  ULONG     TCPOffLoadAvailable;
} ISCSI_Path, *PISCSI_Path;
````


## -struct-fields
<dl>

### -field <b>UniqueConnectionId</b>

<dd>
<p>This is a unique connection identifier that the initiator uses to identify a connection. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in the UniqueConnectionId parameter.  This value is not to be confused with the connection ID (CID).</p>
</dd>

### -field <b>EstimatedLinkSpeed</b>

<dd>
<p>This specifies the connection speed in megabits per second (Mbps).</p>
</dd>

### -field <b>PathWeight</b>

<dd>
<p>This specifies the weight assigned to this path. The value can be any 32-bit number, with a higher number that signifies a higher priority. If more than one path is available, this path weight value is compared against each other path weight and will be prioritized accordingly. For example, if a value of 1 is used for path1 and a value of 2 for path2, path2 has higher priority.</p>
</dd>

### -field <b>PrimaryPath</b>

<dd>
<p>This specifies the state of the path: primary or secondary. If the value is 1, it means the path is the primary path, and if it is 0, it is a secondary path.</p>
</dd>

### -field <b>ConnectionStatus</b>

<dd>
<p>This indicates the status of the connection.</p>
<table>
<tr>
<th>Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>CONNECTION_STATE_CONNECTED (1)</p>
</td>
<td>
<p>The path is connected and active.</p>
</td>
</tr>
<tr>
<td>
<p>CONNECTION_STATE_DISCONNECTED (2)</p>
</td>
<td>
<p>The path is disconnected.</p>
</td>
</tr>
<tr>
<td>
<p>CONNECTION_STATE_RECONNECTING(3)</p>
</td>
<td>
<p>The path is reconnecting.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TCPOffLoadAvailable</b>

<dd>
<p>This indicates whether the connection supports TCP offload or not.</p>
</dd>
</dl>

## -remarks
<p>The iSCSI headers and MOF are included in the platform SDK and WDK.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsimgt.h (include Iscsimgt.h)</dt>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_Path structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
