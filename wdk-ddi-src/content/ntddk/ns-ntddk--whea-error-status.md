---
UID: NS.ntddk._WHEA_ERROR_STATUS
title: WHEA_ERROR_STATUS
author: windows-driver-content
description: The WHEA_ERROR_STATUS union describes generic error codes that are abstracted from the data contained in implementation-specific error registers.
old-location: whea\whea_error_status.htm
old-project: whea
ms.assetid: 5b11112b-e900-4894-a9ce-6895a4fa1956
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_ERROR_STATUS, WHEA_ERROR_STATUS, *PWHEA_ERROR_STATUS
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
req.alt-api: WHEA_ERROR_STATUS
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

# WHEA_ERROR_STATUS structure



## -description
<p>The WHEA_ERROR_STATUS union describes generic error codes that are abstracted from the data contained in implementation-specific error registers.</p>


## -syntax

````
typedef union _WHEA_ERROR_STATUS {
  ULONGLONG ErrorStatus;
  struct {
    ULONGLONG Reserved1  :8;
    ULONGLONG ErrorType  :8;
    ULONGLONG Address  :1;
    ULONGLONG Control  :1;
    ULONGLONG Data  :1;
    ULONGLONG Responder  :1;
    ULONGLONG Requester  :1;
    ULONGLONG FirstError  :1;
    ULONGLONG Overflow  :1;
    ULONGLONG Reserved2  :41;
  };
} WHEA_ERROR_STATUS, *PWHEA_ERROR_STATUS;
````


## -struct-fields
<dl>

### -field ErrorStatus

<dd>
<p>A ULONGLONG representation of the contents of the WHEA_ERROR_STATUS union.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved for system use.</p>
</dd>

### -field ErrorType

<dd>
<p>The type of hardware error that occurred. Possible values are:</p>
<p></p>
<dl>

### -field ERRTYP_INTERNAL

<dd>
<p>An error internal to the component.</p>
</dd>

### -field ERRTYP_BUS

<dd>
<p>A bus error.</p>
</dd>

### -field ERRTYP_MEM

<dd>
<p>A memory error.</p>
</dd>

### -field ERRTYP_TLB

<dd>
<p>A translation lookaside buffer error.</p>
</dd>

### -field ERRTYP_CACHE

<dd>
<p>A cache error.</p>
</dd>

### -field ERRTYP_FUNCTION

<dd>
<p>An error in one or more functional units.</p>
</dd>

### -field ERRTYP_SELFTEST

<dd>
<p>The component failed self test.</p>
</dd>

### -field ERRTYP_FLOW

<dd>
<p>An overflow or underflow of a queue that is internal to the component.</p>
</dd>

### -field ERRTYP_MAP

<dd>
<p>The virtual address was not found on IO-TLB or IO-PDIR.</p>
</dd>

### -field ERRTYP_IMPROPER

<dd>
<p>An improper access error.</p>
</dd>

### -field ERRTYP_UNIMPL

<dd>
<p>An access to a memory address that is not mapped to any component.</p>
</dd>

### -field ERRTYP_LOSSOFLOCKSTEP

<dd>
<p>A loss of lockstep.</p>
</dd>

### -field ERRTYP_RESPONSE

<dd>
<p>A response was received that was not associated with a request.</p>
</dd>

### -field ERRTYP_PARITY

<dd>
<p>A bus parity error.</p>
</dd>

### -field ERRTYP_PROTOCOL

<dd>
<p>A bus protocol error.</p>
</dd>

### -field ERRTYP_PATHERROR

<dd>
<p>A bus path error.</p>
</dd>

### -field ERRTYP_TIMEOUT

<dd>
<p>A bus timeout error.</p>
</dd>

### -field ERRTYP_POISONED

<dd>
<p>A read operation was issued to data that has been corrupted.</p>
</dd>
</dl>
</dd>

### -field Address

<dd>
<p>A single bit that indicates if the error was detected on the address signals or during the address portion of the transaction.</p>
</dd>

### -field Control

<dd>
<p>A single bit that indicates if the error was detected on the control signals or during the control portion of the transaction.</p>
</dd>

### -field Data

<dd>
<p>A single bit that indicates if the error was detected on the data signals or during the data portion of the transaction.</p>
</dd>

### -field Responder

<dd>
<p>A single bit that indicates that the error was detected by the responder of the transaction.</p>
</dd>

### -field Requester

<dd>
<p>A single bit that indicates that the error was detected by the requester of the transaction.</p>
</dd>

### -field FirstError

<dd>
<p>A single bit that indicates that the error is the first error to occur if multiple errors are logged for a section type. Setting of this bit is optional.</p>
</dd>

### -field Overflow

<dd>
<p>A single bit that indicates that additional errors occurred but were not logged due to an overflow of the logging resources.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The WHEA_ERROR_STATUS union provides the capability to abstract information from implementation-specific error registers into generic error codes so that the operating system can process the errors without an intimate knowledge of the underlying platform. This union is derived from the Error Status section of the <a href="http://go.microsoft.com/fwlink/p/?linkid=26730">Intel Itanium Processor Family System Abstraction Layer Specification</a>.</p>

<p>A WHEA_ERROR_STATUS union is contained within the <a href="..\ntddk\ns-ntddk--whea-memory-error-section.md">WHEA_MEMORY_ERROR_SECTION</a>, <a href="..\ntddk\ns-ntddk--whea-pcixbus-error-section.md">WHEA_PCIXBUS_ERROR_SECTION</a>, and <a href="..\ntddk\ns-ntddk--whea-pcixdevice-error-section.md">WHEA_PCIXDEVICE_ERROR_SECTION</a> structures.</p>

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
<a href="..\ntddk\ns-ntddk--whea-memory-error-section.md">WHEA_MEMORY_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-pcixbus-error-section.md">WHEA_PCIXBUS_ERROR_SECTION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-pcixdevice-error-section.md">WHEA_PCIXDEVICE_ERROR_SECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_STATUS union%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
