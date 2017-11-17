---
UID: NE.storport._SES_DOWNLOAD_MICROCODE_STATE
title: SES_DOWNLOAD_MICROCODE_STATE
author: windows-driver-content
description: TBD.
old-location: storage\ses_download_microcode_state.htm
ms.assetid: 5edff312-8373-4d36-b93c-c35fe8c2996a
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
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
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
req.iface: 
req.product: Windows 10 or later.
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

### -field <a id="SesDownloadMcStateNoneInProgress"></a><a id="sesdownloadmcstatenoneinprogress"></a><a id="SESDOWNLOADMCSTATENONEINPROGRESS"></a><b>SesDownloadMcStateNoneInProgress</b>

<dd>
<p>Specifies no microcode download operation is in progress.</p>
</dd>

### -field <a id="SesDownloadMcStateInProgress"></a><a id="sesdownloadmcstateinprogress"></a><a id="SESDOWNLOADMCSTATEINPROGRESS"></a><b>SesDownloadMcStateInProgress</b>

<dd>
<p>Specifies a microcode download operation is in progress.</p>
</dd>

### -field <a id="SesDownloadMcStateCompletedPendingReset"></a><a id="sesdownloadmcstatecompletedpendingreset"></a><a id="SESDOWNLOADMCSTATECOMPLETEDPENDINGRESET"></a><b>SesDownloadMcStateCompletedPendingReset</b>

<dd>
<p>Specifies a microcode download operations completed and is waiting for a hard reset.</p>
</dd>

### -field <a id="SesDownloadMcStateCompletedPendingPowerOn"></a><a id="sesdownloadmcstatecompletedpendingpoweron"></a><a id="SESDOWNLOADMCSTATECOMPLETEDPENDINGPOWERON"></a><b>SesDownloadMcStateCompletedPendingPowerOn</b>

<dd>
<p>Specifies a microcode download operations completed and is waiting for a power on.</p>
</dd>

### -field <a id="SesDownloadMcStateCompletedPendingActivation"></a><a id="sesdownloadmcstatecompletedpendingactivation"></a><a id="SESDOWNLOADMCSTATECOMPLETEDPENDINGACTIVATION"></a><b>SesDownloadMcStateCompletedPendingActivation</b>

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