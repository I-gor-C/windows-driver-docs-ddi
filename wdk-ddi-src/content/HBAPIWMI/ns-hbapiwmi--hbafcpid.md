---
UID: NS.hbapiwmi._HBAFCPID
title: HBAFCPID
author: windows-driver-content
description: The HBAFCPID structure contains information that uniquely identifies a logical unit on a fibre channel network.
old-location: storage\hbafcpid.htm
ms.assetid: a4fa3093-a328-4d90-bc51-0e7a6db1ed58
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBAFCPID
req.alt-loc: hbapiwmi.h
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
ms.keywords: HBAFCPID, HBAFCPID, *PHBAFCPID
req.iface: 
---

# HBAFCPID structure



## -description
<p>The HBAFCPID structure contains information that uniquely identifies a logical unit on a fibre channel network.</p>


## -syntax

````
typedef struct _HBAFCPID {
  ULONG     Fcid;
  UCHAR     NodeWWN[8];
  UCHAR     PortWWN[8];
  ULONGLONG FcpLun;
} HBAFCPID, *PHBAFCPID;
````


## -struct-fields
<dl>

### -field <b>Fcid</b>

<dd>
<p>Contains the identifier that indicates which port is to be queried for information about the logical unit. For a discussion of the values that this member have, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -field <b>NodeWWN</b>

<dd>
<p>Contains the 64 bit world-wide name (WWN) of the node (machine) to which the logical unit is connected. If an HBA has multiple ports and is associated with more than one node, this member will contain a name chosen from among the names of the associated nodes. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -field <b>PortWWN</b>

<dd>
<p>Contains the 64 bit world-wide name of the port to be queried for information about the logical unit. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -field <b>FcpLun</b>

<dd>
<p>Contains a 64-bit fibre channel protocol (FCP) number for the logical unit. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration for this structure in <i>hbapiwm.h</i> after compiling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556039">HBAFCPID WMI Class</a>.</p>

<p>For more information about the fibre channel protocol (FCP), see the T11 committee's <i>dpANS Fibre Channel Protocol for SCSI</i> and <i>Fibre Channel HBA API</i> specifications.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556034">HBAFCPBindingEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBAFCPID structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
