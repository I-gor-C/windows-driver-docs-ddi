---
UID: NE.minitape._SES_DOWNLOAD_MICROCODE_STATE
title: SES_DOWNLOAD_MICROCODE_STATE
author: windows-driver-content
description: TBD.
old-location: storage\ses_download_microcode_state.htm
old-project: storage
ms.assetid: 5edff312-8373-4d36-b93c-c35fe8c2996a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PROCESSOR_NUMBER, PROCESSOR_NUMBER, *PPROCESSOR_NUMBER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: minitape.h
req.include-header: Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1709 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SES_DOWNLOAD_MICROCODE_STATE
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
req.irql: 
req.iface: 
---

# SES_DOWNLOAD_MICROCODE_STATE enumeration



## -description
<p>TBD</p>


## -syntax

````
typedef enum _SES_DOWNLOAD_MICROCODE_STATE { 
  SesDownloadMcStateNoneInProgress              =  0x00,
  SesDownloadMcStateInProgress                  =  0x01,
  SesDownloadMcStateCompletedPendingReset       =  0x11,
  SesDownloadMcStateCompletedPendingPowerOn     = 0x12,
  SesDownloadMcStateCompletedPendingActivation  = 0x13
} SES_DOWNLOAD_MICROCODE_STATE, *PSES_DOWNLOAD_MICROCODE_STATE;
````


## -enum-fields
<dl>

### -field SesDownloadMcStateNoneInProgress

<dd>
<p>Specifies no microcode download operation is in progress.</p>
</dd>

### -field SesDownloadMcStateInProgress

<dd>
<p>Specifies a microcode download operation is in progress.</p>
</dd>

### -field SesDownloadMcStateCompletedPendingReset

<dd>
<p>Specifies a microcode download operations completed and is waiting for a hard reset.</p>
</dd>

### -field SesDownloadMcStateCompletedPendingPowerOn

<dd>
<p>Specifies a microcode download operations completed and is waiting for a power on.</p>
</dd>

### -field SesDownloadMcStateCompletedPendingActivation

<dd>
<p>Specifies a microcode download operations completed and is waiting for activation.</p>
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