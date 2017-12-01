---
UID: NS.ntddpar._PAR_QUERY_INFORMATION
title: PAR_QUERY_INFORMATION
author: windows-driver-content
description: The PAR_QUERY_INFORMATION structure specifies the operating status of a parallel port.
old-location: parports\par_query_information.htm
old-project: parports
ms.assetid: 3115b0c2-0190-4c5c-8b31-dbafddc9c44d
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: PAR_QUERY_INFORMATION, PAR_QUERY_INFORMATION, *PPAR_QUERY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddpar.h
req.include-header: Ntddpar.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PAR_QUERY_INFORMATION
req.alt-loc: ntddpar.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PAR_QUERY_INFORMATION structure



## -description
<p>The PAR_QUERY_INFORMATION structure specifies the operating status of a parallel port.</p>


## -syntax

````
typedef struct _PAR_QUERY_INFORMATION {
  UCHAR Status;
} PAR_QUERY_INFORMATION, *PPAR_QUERY_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Status</b>

<dd>
<p>Specifies the operating status of a parallel port. The value of <b>Status</b> is a bitwise OR of one or more of the following flags:</p>
<p></p>
<dl>

### -field <a id="PARALLEL_INIT"></a><a id="parallel_init"></a>PARALLEL_INIT

<dd></dd>

### -field <a id="PARALLEL_AUTOFEED_"></a><a id="parallel_autofeed_"></a>PARALLEL_AUTOFEED 

<dd></dd>

### -field <a id="PARALLEL_PAPER_EMPTY_"></a><a id="parallel_paper_empty_"></a>PARALLEL_PAPER_EMPTY 

<dd></dd>

### -field <a id="PARALLEL_OFF_LINE_"></a><a id="parallel_off_line_"></a>PARALLEL_OFF_LINE 

<dd></dd>

### -field <a id="PARALLEL_POWER_OFF"></a><a id="parallel_power_off"></a>PARALLEL_POWER_OFF

<dd></dd>

### -field <a id="PARALLEL_NOT_CONNECTED_"></a><a id="parallel_not_connected_"></a>PARALLEL_NOT_CONNECTED 

<dd></dd>

### -field <a id="PARALLEL_BUSY_"></a><a id="parallel_busy_"></a>PARALLEL_BUSY 

<dd></dd>

### -field <a id="PARALLEL_SELECTED_"></a><a id="parallel_selected_"></a>PARALLEL_SELECTED 

<dd></dd>
</dl>
</dd>
</dl>

## -remarks
<p>This structure is used with an <a href="..\ntddpar\ni-ntddpar-ioctl-par-query-information.md">IOCTL_PAR_QUERY_INFORMATION</a> request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddpar.h (include Ntddpar.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddpar\ni-ntddpar-ioctl-par-query-information.md">IOCTL_PAR_QUERY_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddpar\ni-ntddpar-ioctl-par-set-information.md">IOCTL_PAR_SET_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddpar\ns-ntddpar--par-set-information.md">PAR_SET_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PAR_QUERY_INFORMATION structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
