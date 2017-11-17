---
UID: NE.rilapitypes.RILNOTIFICATIONFILTERMASK
title: RILNOTIFICATIONFILTERMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilnotificationfiltermask_2.htm
ms.assetid: 00d083af-f2c1-4ad5-803a-5981ed70035f
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILNOTIFICATIONFILTERMASK
req.alt-loc: rilapitypes.h
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILNOTIFICATIONFILTERMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILNOTIFICATIONFILTERMASK { 
  RIL_NFS_SIGNALQUALITY,
  RIL_NFS_REGSTATUS_RATKIND,
  RIL_NFS_LOCATIONUPDATE,
  RIL_NFS_ALL
} RILNOTIFICATIONFILTERMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_NFS_SIGNALQUALITY"></a><a id="ril_nfs_signalquality"></a><b>RIL_NFS_SIGNALQUALITY</b>

<dd></dd>

### -field <a id="RIL_NFS_REGSTATUS_RATKIND"></a><a id="ril_nfs_regstatus_ratkind"></a><b>RIL_NFS_REGSTATUS_RATKIND</b>

<dd></dd>

### -field <a id="RIL_NFS_LOCATIONUPDATE"></a><a id="ril_nfs_locationupdate"></a><b>RIL_NFS_LOCATIONUPDATE</b>

<dd></dd>

### -field <a id="RIL_NFS_ALL"></a><a id="ril_nfs_all"></a><b>RIL_NFS_ALL</b>

<dd></dd>
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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>