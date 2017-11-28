---
UID: NS.ntifs._FILE_MAILSLOT_SET_INFORMATION
title: FILE_MAILSLOT_SET_INFORMATION
author: windows-driver-content
description: The FILE_MAILSLOT_SET_INFORMATION structure is used to set a value on a mailslot.
old-location: ifsk\file_mailslot_set_information.htm
old-project: ifsk
ms.assetid: 65104303-5041-45e7-bd59-bb78dde1dffd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_MAILSLOT_SET_INFORMATION, FILE_MAILSLOT_SET_INFORMATION, *PFILE_MAILSLOT_SET_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_MAILSLOT_SET_INFORMATION
req.alt-loc: ntifs.h
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

# FILE_MAILSLOT_SET_INFORMATION structure



## -description
<p>The <b>FILE_MAILSLOT_SET_INFORMATION</b> structure is used to set a value on a   mailslot.</p>


## -syntax

````
typedef struct _FILE_MAILSLOT_SET_INFORMATION {
  PLARGE_INTEGER  ReadTimeout;
} FILE_MAILSLOT_SET_INFORMATION, *PFILE_MAILSLOT_SET_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>ReadTimeout</b>

<dd>
<p>
The time, in milliseconds, that a read operation can wait for a message to be written to the mailslot before a time-out occurs. A value of –1 requests that the read wait forever for a message without timing out. A value of 0 requests that the read not wait and return immediately whether a pending message is available to be read or not.
</p>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="base.mailslots">Mailslots</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>