---
UID: NS.smclib._SCARD_READER_CAPABILITIES
title: SCARD_READER_CAPABILITIES
author: windows-driver-content
description: The SCARD_READER_CAPABILITIES structure holds state information about the smart card reader.
old-location: smartcrd\scard_reader_capabilities.htm
old-project: smartcrd
ms.assetid: f55b74d0-d545-419a-87fb-c320f789aaf4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SCARD_READER_CAPABILITIES, SCARD_READER_CAPABILITIES, *PSCARD_READER_CAPABILITIES
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
req.alt-api: SCARD_READER_CAPABILITIES
req.alt-loc: Smclib.h
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

# SCARD_READER_CAPABILITIES structure



## -description
<p>The SCARD_READER_CAPABILITIES structure holds state information about the smart card reader. </p>


## -syntax

````
typedef struct {
  ULONG  SupportedProtocols;
  ULONG  ReaderType;
  ULONG  Reserved;
  ULONG  MechProperties;
  ULONG  CurrentState;
  ULONG  Channel;
  struct {
    ULONG Default;
    ULONG Max;
  } CLKFrequency;
  struct {
    ULONG Default;
    ULONG Max;
  } DataRate;
  ULONG  MaxIFSD;
  ULONG  PowerMgmtSupport;
  ULONG  CardConfiscated;
  struct {
    PULONG List;
    UCHAR  Entries;
  } DataRatesSupported;
  struct {
    PULONG List;
    UCHAR  Entries;
  } CLKFrequenciesSupported;
  UCHAR  Reserved1[100 - sizeof(ULONG) -  sizeof(struct _DataRatesSupported) - sizeof(struct _CLKFrequenciesSupported)];
} SCARD_READER_CAPABILITIES, *PSCARD_READER_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>SupportedProtocols</b>

<dd>
<p>Must be set to a bitmask that reflects the asynchronous or synchronous protocols that the card reader and card reader driver support. This member is required.   </p>
</dd>

### -field <b>ReaderType</b>

<dd>
<p>This member contains the reader type and is required. This member can have one of the values in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_SERIAL</p>
</td>
<td>
<p>Serial reader</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_PCMCIA</p>
</td>
<td>
<p>PCMCIA reader</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_KEYBOARD</p>
</td>
<td>
<p>Keyboard-attached reader</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_USB</p>
</td>
<td>
<p>USB reader</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_PARALELL</p>
</td>
<td>
<p>Parallel reader </p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_SCSI</p>
</td>
<td>
<p>SCSI reader </p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_IDE</p>
</td>
<td>
<p>IDE reader </p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_TPM</p>
</td>
<td>
<p>Reader that uses a TPM chip for key material storage and cryptographic operations</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_TYPE_VENDOR</p>
</td>
<td>
<p>Reader that uses a proprietary vendor bus </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <b>MechProperties</b>

<dd>
<p>Contains a value that is formed by taking a bitwise OR of all applicable reader properties shown in the following table. This member is optional. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SCARD_READER_SWALLOWS</p>
</td>
<td>
<p>Reader has a swallowing mechanism.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_EJECTS</p>
</td>
<td>
<p>Reader can eject the smart card.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_READER_CONFISCATES</p>
</td>
<td>
<p>Reader can swallow the smart card.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CurrentState</b>

<dd>
<p>This member contains the status of the card and is required. This member can have one of the values listed in the following table.</p>
<table>
<tr>
<th>Status</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SCARD_UNKNOWN</p>
</td>
<td>
<p>The reader does not have information about the status.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_ABSENT</p>
</td>
<td>
<p>No smart card is inserted.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_PRESENT</p>
</td>
<td>
<p>A smart card is inserted.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_SWALLOWED</p>
</td>
<td>
<p>A smart card is inserted and the reader has swallowed it.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_POWERED</p>
</td>
<td>
<p>The smart card is turned on, but the reader does not recognize its mode.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_NEGOTIABLE</p>
</td>
<td>
<p>A smart card is inserted and awaits protocol negotiation.</p>
</td>
</tr>
<tr>
<td>
<p>SCARD_SPECIFIC</p>
</td>
<td>
<p>A smart card is inserted and a protocol has been selected.</p>
</td>
</tr>
</table>
<p> </p>
<p>Access to this field must be sequentialized by using the spin lock pointed to by the <b>OsData-&gt;SpinLock</b> member of <a href="..\smclib\ns-smclib--smartcard-extension.md">SMARTCARD_EXTENSION</a>. </p>
</dd>

### -field <b>Channel</b>

<dd>
<p>Contains the logical channel number. This member is optional. The exact meaning of this member depends on the type of smart card, as shown in the following table. </p>
<table>
<tr>
<th>Type of smart card</th>
<th>Meaning of value in channel field</th>
</tr>
<tr>
<td>
<p>Serial reader</p>
</td>
<td>
<p>Port number</p>
</td>
</tr>
<tr>
<td>
<p>Parallel reader</p>
</td>
<td>
<p>Port number</p>
</td>
</tr>
<tr>
<td>
<p>SCSI reader</p>
</td>
<td>
<p>SCSI ID</p>
</td>
</tr>
<tr>
<td>
<p>Keyboard reader</p>
</td>
<td>
<p>0</p>
</td>
</tr>
<tr>
<td>
<p>USB reader</p>
</td>
<td>
<p>Device number</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information, see Part 3 of the <i>Interoperability Specification for ICCs and Personal Computer Systems</i>. </p>
</dd>

### -field <b>CLKFrequency</b>

<dd>
<p>
      A structure with the following members:</p>
<dl>

### -field <b>Default</b>

<dd>
<p>Contains the standard clock frequency at which the reader runs, in kilohertz, and encoded in little-endian format. For example, 3.58 MHz is encoded as 3580. This member is required. </p>
</dd>

### -field <b>Max</b>

<dd>
<p>Contains the maximum clock frequency at which the reader can run, in kilohertz, and encoded in little-endian format. This member is required. </p>
</dd>
</dl>
</dd>

### -field <b>DataRate</b>

<dd>
<p>
      A structure with the following members:
     </p>
<dl>

### -field <b>Default</b>

<dd>
<p>Contains the standard data rate of the reader, in units of bits per second, and encoded in little-endian format. This member is required. </p>
</dd>

### -field <b>Max</b>

<dd>
<p>Contains the maximum data rate of the reader, in units of bits per second, and encoded in little-endian format. This member is required.  </p>
</dd>
</dl>
</dd>

### -field <b>MaxIFSD</b>

<dd>
<p>Contains the maximum buffer size of the reader. This value informs the smart card at the beginning of a T=1 transmission of the maximum number of bytes that can be received in one packet. This member is required.  </p>
</dd>

### -field <b>PowerMgmtSupport</b>

<dd>
<p>Indicates the type of power management that the card supports. A value of zero indicates that the smart card does not support power management. </p>
</dd>

### -field <b>CardConfiscated</b>

<dd>
<p>If <b>TRUE</b>, indicates that the smart card was confiscated.</p>
</dd>

### -field <b>DataRatesSupported</b>

<dd>
<p>
      A structure with the following members:
     </p>
<dl>

### -field <b>List</b>

<dd>
<p>Contains a list of data rates, in bits per second, that are supported by the reader. This member is used with the PTS request. The reader driver usually sets this member to a pointer to a static array of unsigned long values that contain the supported data rates. If the reader does not support different data rates, leave this member empty. This member is optional.</p>
</dd>

### -field <b>Entries</b>

<dd>
<p>Contains the number of linked list entries in DataRatesSupported.List. This member is optional. </p>
</dd>
</dl>
</dd>

### -field <b>CLKFrequenciesSupported</b>

<dd>
<p>
      A structure with the following members:
      
     </p>
<dl>

### -field <b>List</b>

<dd>
<p>Contains a list of clock frequencies, in kilohertz, that are supported by the reader. This member is used with the PTS request. The driver usually sets this member to a pointer to a static array of unsigned long values that contain the supported clock frequencies. If the reader does not support different clock frequencies, leave this member empty. This member is optional. </p>
</dd>

### -field <b>Entries</b>

<dd>
<p>Contains the number of linked list entries of CLKFrquenciesSupported.List. This member is optional. </p>
</dd>
</dl>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>This structure must be maintained by the smart card reader driver. </p>

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