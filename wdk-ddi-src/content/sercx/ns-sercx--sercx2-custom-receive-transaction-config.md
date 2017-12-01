---
UID: NS.sercx._SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG
title: SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG
author: windows-driver-content
description: The SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new custom-receive-transaction object.
old-location: serports\sercx2_custom_receive_transaction_config.htm
old-project: serports
ms.assetid: 7D9E4F33-FCEE-4783-AE33-DCD3CB0286AE
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sercx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG
req.alt-loc: 2.0\Sercx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level.
req.iface: 
req.product: Windows 10 or later.
---

# SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG structure



## -description
<p>The <b>SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG</b> structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new custom-receive-transaction object.</p>


## -syntax

````
typedef struct _SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG {
  ULONG                                                              Size;
  PFN_SERCX2_CUSTOM_RECEIVE_TRANSACTION_INITIALIZE                   EvtSerCx2CustomReceiveTransactionInitialize;
  PFN_SERCX2_CUSTOM_RECEIVE_TRANSACTION_START                        EvtSerCx2CustomReceiveTransactionStart;
  PFN_SERCX2_CUSTOM_RECEIVE_TRANSACTION_CLEANUP                      EvtSerCx2CustomReceiveTransactionCleanup;
  PFN_SERCX2_CUSTOM_RECEIVE_TRANSACTION_ENABLE_NEW_DATA_NOTIFICATION EvtSerCx2CustomReceiveTransactionEnableNewDataNotification;
  PFN_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS               EvtSerCx2CustomReceiveTransactionQueryProgress;
} SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG, *PSERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure. The <a href="..\sercx\nf-sercx-sercx2customreceivetransactioncreate.md">SerCx2CustomReceiveTransactionCreate</a> method uses this member to determine which version of the structure the caller is using. The size of this structure might change in future versions of the Sercx.h header file.</p>
</dd>

### -field <b>EvtSerCx2CustomReceiveTransactionInitialize</b>

<dd>
<p>A pointer to the driver-implemented <a href="..\sercx\nc-sercx-evt-sercx2-custom-receive-transaction-initialize.md">EvtSerCx2CustomReceiveTransactionInitialize</a> event callback function. This member is optional and can be set to <b>NULL</b> to indicate that the driver does not implement the function.</p>
</dd>

### -field <b>EvtSerCx2CustomReceiveTransactionStart</b>

<dd>
<p>A pointer to the driver-implemented <a href="..\sercx\nc-sercx-evt-sercx2-custom-receive-transaction-start.md">EvtSerCx2CustomReceiveTransactionStart</a> event callback function. This member must point to a valid function.</p>
</dd>

### -field <b>EvtSerCx2CustomReceiveTransactionCleanup</b>

<dd>
<p>A pointer to the driver-implemented <a href="..\sercx\nc-sercx-evt-sercx2-custom-receive-transaction-cleanup.md">EvtSerCx2CustomReceiveTransactionCleanup</a> event callback function. This member is optional and can be set to <b>NULL</b> to indicate that the driver does not implement the function.</p>
</dd>

### -field <b>EvtSerCx2CustomReceiveTransactionEnableNewDataNotification</b>

<dd>
<p>A pointer to the driver-implemented <a href="serports.evtsercx2customreceivetransactionenablenewdatanotification">EvtSerCx2CustomReceiveTransactionEnableNewDataNotification</a> event callback function. This member is optional and can be set to <b>NULL</b> to indicate that the driver does not implement the function.</p>
</dd>

### -field <b>EvtSerCx2CustomReceiveTransactionQueryProgress</b>

<dd>
<p>A pointer to the driver-implemented <a href="serports.evtsercx2customreceivetransactionqueryprogress">EvtSerCx2CustomReceiveTransactionQueryProgress</a> event callback function. This member must point to a valid function.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\sercx\nf-sercx-sercx2customreceivetransactioncreate.md">SerCx2CustomReceiveTransactionCreate</a> method accepts a pointer to a <b>SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG</b> structure as an input parameter. Before calling <b>SerCx2CustomReceiveTransactionInitialize</b>, call the <a href="..\sercx\nf-sercx-sercx2-custom-receive-transaction-config-init.md">SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG_INIT</a> function to initialize this structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>2.0\Sercx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-custom-receive-transaction-cleanup.md">EvtSerCx2CustomReceiveTransactionCleanup</a>
</dt>
<dt>
<a href="serports.evtsercx2customreceivetransactionenablenewdatanotification">EvtSerCx2CustomReceiveTransactionEnableNewDataNotification</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-custom-receive-transaction-initialize.md">EvtSerCx2CustomReceiveTransactionInitialize</a>
</dt>
<dt>
<a href="serports.evtsercx2customreceivetransactionqueryprogress">EvtSerCx2CustomReceiveTransactionQueryProgress</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-custom-receive-transaction-start.md">EvtSerCx2CustomReceiveTransactionStart</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2-custom-receive-transaction-config-init.md">SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG_INIT</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2customreceivetransactioncreate.md">SerCx2CustomReceiveTransactionCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
