---
UID: NS.scsi.PRT_PARAMETER_DATA
title: PRT_PARAMETER_DATA
author: windows-driver-content
description: The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command.
old-location: storage\rt_parameter_data.htm
old-project: storage
ms.assetid: EB23D502-87E4-48B1-B1DC-0B215AB361C8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PRT_PARAMETER_DATA, RT_PARAMETER_DATA, *PRT_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsi.h
req.include-header: Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1709 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RT_PARAMETER_DATA
req.alt-loc: scsi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PRT_PARAMETER_DATA structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>RT_PARAMETER_DATA</b> structure contains the parameter data for the report timestamp command. </p>


## -syntax

````
typedef struct _RT_PARAMETER_DATA {
  UCHAR     ParameterDataLength[2];
  UCHAR Origin  :3;
  UCHAR Reserved1  :5;
  UCHAR Reserved2;
  UCHAR Timestamp[6];
  UCHAR Reserved3[2];
} RT_PARAMETER_DATA, *PRT_PARAMETER_DATA;
````


## -struct-fields
<dl>

### -field     ParameterDataLength

<dd>
<p>Indicates the number of bytes that follow in the parameter data.</p>
</dd>

### -field Origin

<dd>
<p>Indicates the most recent event that initialized the returned device clock.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Device clock initialized to zero at power on or as the result of a hard reset.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 2

</dl>
</td>
<td width="60%">
<p>Device clock initialized by the SET TIMESTAMP command.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 3

</dl>
</td>
<td width="60%">
<p>Device clock initialized by an unknown method.</p>
</td>
</tr>
<tr>
<td width="40%"><a id=""></a><dl>

### -field 


### -field 4 to 7

</dl>
</td>
<td width="60%">
<p>Reserved for future use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Reserved1

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Timestamp

<dd>
<p>Contains the current value of a device clock.</p>
</dd>

### -field Reserved3

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10, version 1709 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsi.h (include Minitape.h or Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.st_parameter_data">ST_PARAMETER_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20RT_PARAMETER_DATA structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
