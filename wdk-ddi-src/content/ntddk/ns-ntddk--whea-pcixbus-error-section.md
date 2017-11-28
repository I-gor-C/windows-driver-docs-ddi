---
UID: NS.ntddk._WHEA_PCIXBUS_ERROR_SECTION
title: WHEA_PCIXBUS_ERROR_SECTION
author: windows-driver-content
description: The WHEA_PCIXBUS_ERROR_SECTION structure describes PCI or PCI-X bus error data.
old-location: whea\whea_pcixbus_error_section.htm
old-project: whea
ms.assetid: f79071e3-7146-49c4-a730-ee13fde4f0d4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_PCIXBUS_ERROR_SECTION, WHEA_PCIXBUS_ERROR_SECTION, *PWHEA_PCIXBUS_ERROR_SECTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_PCIXBUS_ERROR_SECTION
req.alt-loc: ntddk.h
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

# WHEA_PCIXBUS_ERROR_SECTION structure



## -description
<p>The WHEA_PCIXBUS_ERROR_SECTION structure describes PCI or PCI-X bus error data.</p>


## -syntax

````
typedef struct _WHEA_PCIXBUS_ERROR_SECTION {
  WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS ValidBits;
  WHEA_ERROR_STATUS                    ErrorStatus;
  USHORT                               ErrorType;
  WHEA_PCIXBUS_ID                      BusId;
  ULONG                                Reserved;
  ULONGLONG                            BusAddress;
  ULONGLONG                            BusData;
  WHEA_PCIXBUS_COMMAND                 BusCommand;
  ULONGLONG                            RequesterId;
  ULONGLONG                            CompleterId;
  ULONGLONG                            TargetId;
} WHEA_PCIXBUS_ERROR_SECTION, *PWHEA_PCIXBUS_ERROR_SECTION;
````


## -struct-fields
<dl>

### -field <b>ValidBits</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560585">WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS</a> union that specifies which members of this structure contain valid data.</p>
</dd>

### -field <b>ErrorStatus</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560514">WHEA_ERROR_STATUS</a> structure that contains PCI or PCI-X bus error status data.</p>
<p>This member contains valid data only if the <b>ValidBits.ErrorStatus</b> bit is set.</p>
</dd>

### -field <b>ErrorType</b>

<dd>
<p>The type of PCI or PCI-X bus error that occurred. Possible values are:</p>
<p></p>
<dl>

### -field <a id="PCIXBUS_ERRTYPE_UNKNOWN"></a><a id="pcixbus_errtype_unknown"></a>PCIXBUS_ERRTYPE_UNKNOWN

<dd>
<p>An unknown or platform-specific error.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_DATAPARITY"></a><a id="pcixbus_errtype_dataparity"></a>PCIXBUS_ERRTYPE_DATAPARITY

<dd>
<p>A data parity error.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_SYSTEM"></a><a id="pcixbus_errtype_system"></a>PCIXBUS_ERRTYPE_SYSTEM

<dd>
<p>A system error.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_MASTERABORT"></a><a id="pcixbus_errtype_masterabort"></a>PCIXBUS_ERRTYPE_MASTERABORT

<dd>
<p>A master abort.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_BUSTIMEOUT"></a><a id="pcixbus_errtype_bustimeout"></a>PCIXBUS_ERRTYPE_BUSTIMEOUT

<dd>
<p>A bus timeout, or no device is present.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_MASTERDATAPARITY"></a><a id="pcixbus_errtype_masterdataparity"></a>PCIXBUS_ERRTYPE_MASTERDATAPARITY

<dd>
<p>A master data parity error.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_ADDRESSPARITY"></a><a id="pcixbus_errtype_addressparity"></a>PCIXBUS_ERRTYPE_ADDRESSPARITY

<dd>
<p>An address parity error.</p>
</dd>

### -field <a id="PCIXBUS_ERRTYPE_COMMANDPARITY"></a><a id="pcixbus_errtype_commandparity"></a>PCIXBUS_ERRTYPE_COMMANDPARITY

<dd>
<p>A command parity error.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>ValidBits.ErrorType</b> bit is set.</p>
</dd>

### -field <b>BusId</b>

<dd>
<p>A WHEA_PCIXBUS_ID union that identifies the bus where the error occurred. The WHEA_PCIXBUS_ID union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_PCIXBUS_ID {
  struct {
    UCHAR  BusNumber;
    UCHAR  BusSegment;
  };
  USHORT  AsUSHORT;
} WHEA_PCIXBUS_ID, *PWHEA_PCIXBUS_ID;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="BusNumber"></a><a id="busnumber"></a><a id="BUSNUMBER"></a><b>BusNumber</b>

<dd>
<p>The bus number.</p>
</dd>

### -field <a id="BusSegment"></a><a id="bussegment"></a><a id="BUSSEGMENT"></a><b>BusSegment</b>

<dd>
<p>The bus segment.</p>
</dd>

### -field <a id="AsUSHORT"></a><a id="asushort"></a><a id="ASUSHORT"></a><b>AsUSHORT</b>

<dd>
<p>A USHORT representation of the contents of the WHEA_PCIXBUS_ID union.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>ValidBits.BusId</b> bit is set.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>BusAddress</b>

<dd>
<p>The memory or I/O address on the bus when the error occurred.</p>
<p>This member contains valid data only if the <b>ValidBits.BusAddress</b> bit is set.</p>
</dd>

### -field <b>BusData</b>

<dd>
<p>The data on the bus when the error occurred.</p>
<p>This member contains valid data only if the <b>ValidBits.BusData</b> bit is set.</p>
</dd>

### -field <b>BusCommand</b>

<dd>
<p>A WHEA_PCIXBUS_COMMAND union that contains the bus command when the error occurred. The WHEA_PCIXBUS_COMMAND union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_PCIXBUS_COMMAND {
  struct {
    ULONGLONG  Command:56;
    ULONGLONG  PCIXCommand:1;
    ULONGLONG  Reserved:7;
  };
  ULONGLONG  AsULONGLONG;
} WHEA_PCIXBUS_COMMAND, *PWHEA_PCIXBUS_COMMAND;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="Command"></a><a id="command"></a><a id="COMMAND"></a><b>Command</b>

<dd>
<p>The PCI or PCI-X bus command.</p>
</dd>

### -field <a id="PCIXCommand"></a><a id="pcixcommand"></a><a id="PCIXCOMMAND"></a><b>PCIXCommand</b>

<dd>
<p>A single bit that indicates that the command is a PCI-X command.</p>
</dd>

### -field <a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="AsULONGLONG"></a><a id="asulonglong"></a><a id="ASULONGLONG"></a><b>AsULONGLONG</b>

<dd>
<p>A ULONGLONG representation of the contents of the WHEA_PCIXBUS_COMMAND union.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>ValidBits.BusCommand</b> bit is set.</p>
</dd>

### -field <b>RequesterId</b>

<dd>
<p>An identifier that uniquely identifies the requester that is associated with the error.</p>
<p>This member contains valid data only if the <b>ValidBits.RequesterId</b> bit is set.</p>
</dd>

### -field <b>CompleterId</b>

<dd>
<p>An identifier that uniquely identifies the PCI bus responder that is associated with the error.</p>
<p>This member contains valid data only if the <b>ValidBits.CompleterId</b> bit is set.</p>
</dd>

### -field <b>TargetId</b>

<dd>
<p>An identifier that uniquely identifies the intended target of the PCI bus command.</p>
<p>This member contains valid data only if the <b>ValidBits.TargetId</b> bit is set.</p>
</dd>
</dl>

## -remarks
<p>The WHEA_PCIXBUS_ERROR_SECTION structure describes the error data that is contained in a PCI/PCI-X bus error section of an <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>. An error record contains a PCI/PCI-X bus error section only if the <b>SectionType </b>member of one of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structures that describe the error record sections for that error record contains PCIXBUS_ERROR_SECTION_GUID.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560514">WHEA_ERROR_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560585">WHEA_PCIXBUS_ERROR_SECTION_VALIDBITS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PCIXBUS_ERROR_SECTION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
