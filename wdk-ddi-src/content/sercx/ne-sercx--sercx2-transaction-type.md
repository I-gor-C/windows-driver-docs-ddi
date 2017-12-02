---
UID: NE.sercx._SERCX2_TRANSACTION_TYPE
title: SERCX2_TRANSACTION_TYPE
author: windows-driver-content
description: The SERCX2_TRANSACTION_TYPE enumeration defines constants that indicate the type of data-transfer mechanism to use to perform an I/O transaction.
old-location: serports\sercx2_transaction_type.htm
old-project: serports
ms.assetid: 9F50CA34-DDEA-49E4-8149-B92D00476720
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SENSOR_VALUE_PAIR, SENSOR_VALUE_PAIR, *PSENSOR_VALUE_PAIR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sercx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SERCX2_TRANSACTION_TYPE
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
req.irql: Called at IRQL <= DISPATCH_LEVEL.
req.iface: 
req.product: Windows 10 or later.
---

# SERCX2_TRANSACTION_TYPE enumeration



## -description
<p>The <b>SERCX2_TRANSACTION_TYPE</b> enumeration defines constants that indicate the type of data-transfer mechanism to use to perform an I/O transaction.</p>


## -syntax

````
typedef enum _SERCX2_TRANSACTION_TYPE { 
  SerCx2TransactionTypeDefault,
  SerCx2TransactionTypePio,
  SerCx2TransactionTypeSystemDma,
  SerCx2TransactionTypeCustom
} SERCX2_TRANSACTION_TYPE;
````


## -enum-fields
<dl>

### -field SerCx2TransactionTypeDefault

<dd>
<p>Let SerCx2 decide what type of data transfer to use for the I/O transaction.</p>
</dd>

### -field SerCx2TransactionTypePio

<dd>
<p>Use programmed I/O (PIO) to perform the I/O transaction.</p>
</dd>

### -field SerCx2TransactionTypeSystemDma

<dd>
<p>Use system DMA to perform the I/O transaction.</p>
</dd>

### -field SerCx2TransactionTypeCustom

<dd>
<p>Use the custom data-transfer mechanism to perform the I/O transaction.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\sercx\nc-sercx-evt-sercx2-select-next-receive-transaction-type.md">EvtSerCx2SelectNextReceiveTransactionType</a> and <a href="..\sercx\nc-sercx-evt-sercx2-select-next-transmit-transaction-type.md">EvtSerCx2SelectNextTransmitTransactionType</a> event callback functions return <b>SERCX2_TRANSACTION_TYPE</b> enumeration values.</p>

## -requirements
<table>
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
<a href="..\sercx\nc-sercx-evt-sercx2-select-next-receive-transaction-type.md">EvtSerCx2SelectNextReceiveTransactionType</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-select-next-transmit-transaction-type.md">EvtSerCx2SelectNextTransmitTransactionType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20SERCX2_TRANSACTION_TYPE enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
