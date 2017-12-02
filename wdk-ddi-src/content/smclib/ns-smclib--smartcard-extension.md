---
UID: NS.smclib._SMARTCARD_EXTENSION
title: SMARTCARD_EXTENSION
author: windows-driver-content
description: The SMARTCARD_EXTENSION structure is used by both the smart card reader driver and the smart card driver library to access all other smart card data structures.
old-location: smartcrd\smartcard_extension.htm
old-project: smartcrd
ms.assetid: 057d82a8-ce5d-416f-b753-297dcbac27b8
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SMARTCARD_EXTENSION,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SMARTCARD_EXTENSION
req.alt-loc: smclib.h
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
req.product: Windows 10 or later.
---

# SMARTCARD_EXTENSION structure



## -description
<p>The <b>SMARTCARD_EXTENSION</b> structure is used by both the smart card reader driver and the smart card driver library to access all other smart card data structures.</p>


## -syntax

````
typedef struct _SMARTCARD_EXTENSION {
  ULONG                     Version;
  VENDOR_ATTR               VendorAttr;
  NTSTATUS                  (*ReaderFunction[16])(PSMARTCARD_EXTENSION);
  SCARD_CARD_CAPABILITIES   CardCapabilities;
  ULONG                     LastError;
  struct {
    PULONG Information;
    PUCHAR RequestBuffer;
    ULONG  RequestBufferLength;
    PUCHAR ReplyBuffer;
    ULONG  ReplyBufferLength;
  } IoRequest;
  ULONG                     MajorIoControlCode;
  ULONG                     MinorIoControlCode;
  POS_DEP_DATA              OsData;
  SCARD_READER_CAPABILITIES ReaderCapabilities;
  PREADER_EXTENSION         ReaderExtension;
  SMARTCARD_REPLY           SmartcardReply;
  SMARTCARD_REQUEST         SmartcardRequest;
  T0_DATA                   T0;
  T1_DATA                   T1;
  ULONG                     Reserved[25];
} SMARTCARD_EXTENSION, *PSMARTCARD_EXTENSION;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>Indicates the version of this structure. </p>
</dd>

### -field VendorAttr

<dd>
<p>Contains information that identifies the reader driver, such as the vendor name, unit number, and serial number. </p>
</dd>

### -field ReaderFunction

<dd>
<p>A pointer to an array of callback functions for readers.</p>
</dd>

### -field CardCapabilities

<dd>
<p>Contains capabilities of the inserted smart card. </p>
</dd>

### -field LastError

<dd>
<p>Not used.</p>
</dd>

### -field IoRequest

<dd>
<p>
      A structure with the following members:
      
     </p>
<dl>

### -field Information

<dd>
<p>Contains the number of bytes returned. </p>
</dd>

### -field RequestBuffer

<dd>
<p>A pointer to the data in the user's I/O request to be sent to the card. </p>
</dd>

### -field RequestBufferLength

<dd>
<p>Indicates the number of bytes to send to the card. </p>
</dd>

### -field ReplyBuffer

<dd>
<p>A pointer to the buffer that holds the data that is returned by the I/O request. </p>
</dd>

### -field ReplyBufferLength

<dd>
<p>Indicates the number of bytes of the data that are returned by the I/O request. </p>
</dd>
</dl>
</dd>

### -field MajorIoControlCode

<dd>
<p>Contains the major I/O control code. </p>
</dd>

### -field MinorIoControlCode

<dd>
<p>Contains the minor I/O control code. </p>
</dd>

### -field OsData

<dd>
<p>Contains information that is specific to the operating system and the driver type. </p>
</dd>

### -field ReaderCapabilities

<dd>
<p>Contains the capabilities of the keyboard reader. </p>
</dd>

### -field ReaderExtension

<dd>
<p>Contains data that is specifc to the smart card reader. </p>
</dd>

### -field SmartcardReply

<dd>
<p>Contains data that comes from the reader. </p>
</dd>

### -field SmartcardRequest

<dd>
<p>Contains the current command and the data that is sent to the smart card. </p>
</dd>

### -field T0

<dd>
<p>Contains the data for use with the T=0 protocol. </p>
</dd>

### -field T1

<dd>
<p>Contains the data that is used with the T=1 protocol. </p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>This structure is passed to all callback functions.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
</table>