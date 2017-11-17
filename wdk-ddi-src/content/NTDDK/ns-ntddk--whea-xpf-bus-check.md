---
UID: NS.ntddk._WHEA_XPF_BUS_CHECK
title: WHEA_XPF_BUS_CHECK
author: windows-driver-content
description: The WHEA_XPF_BUS_CHECK union describes bus error information for an x86 or x64 processor.
old-location: whea\whea_xpf_bus_check.htm
ms.assetid: 7886a796-2755-4367-bbbd-2017e7900bf4
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_XPF_BUS_CHECK
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
ms.keywords: WHEA_XPF_BUS_CHECK, WHEA_XPF_BUS_CHECK, *PWHEA_XPF_BUS_CHECK
req.iface: 
---

# WHEA_XPF_BUS_CHECK structure



## -description
<p>The WHEA_XPF_BUS_CHECK union describes bus error information for an x86 or x64 processor.</p>


## -syntax

````
typedef union _WHEA_XPF_BUS_CHECK {
  struct {
    ULONGLONG TransactionTypeValid  :1;
    ULONGLONG OperationValid  :1;
    ULONGLONG LevelValid  :1;
    ULONGLONG ProcessorContextCorruptValid  :1;
    ULONGLONG UncorrectedValid  :1;
    ULONGLONG PreciseIPValid  :1;
    ULONGLONG RestartableIPValid  :1;
    ULONGLONG OverflowValid  :1;
    ULONGLONG ParticipationValid  :1;
    ULONGLONG TimeoutValid  :1;
    ULONGLONG AddressSpaceValid  :1;
    ULONGLONG ReservedValid  :5;
    ULONGLONG TransactionType  :2;
    ULONGLONG Operation  :4;
    ULONGLONG Level  :3;
    ULONGLONG ProcessorContextCorrupt  :1;
    ULONGLONG Uncorrected  :1;
    ULONGLONG PreciseIP  :1;
    ULONGLONG RestartableIP  :1;
    ULONGLONG Overflow  :1;
    ULONGLONG Participation  :2;
    ULONGLONG Timeout  :1;
    ULONGLONG AddressSpace  :2;
    ULONGLONG Reserved  :29;
  };
  ULONGLONG XpfBusCheck;
} WHEA_XPF_BUS_CHECK, *PWHEA_XPF_BUS_CHECK;
````


## -struct-fields
<dl>

### -field <b>TransactionTypeValid</b>

<dd>
<p>A single bit that indicates that the <b>TransactionType</b> member contains valid data.</p>
</dd>

### -field <b>OperationValid</b>

<dd>
<p>A single bit that indicates that the <b>Operation</b> member contains valid data.</p>
</dd>

### -field <b>LevelValid</b>

<dd>
<p>A single bit that indicates that the <b>Level</b> member contains valid data.</p>
</dd>

### -field <b>ProcessorContextCorruptValid</b>

<dd>
<p>A single bit that indicates that the <b>ProcessorContextCorrupt</b> member contains valid data.</p>
</dd>

### -field <b>UncorrectedValid</b>

<dd>
<p>A single bit that indicates that the <b>Uncorrected </b>member contains valid data.</p>
</dd>

### -field <b>PreciseIPValid</b>

<dd>
<p>A single bit that indicates that the <b>PreciseIP</b> member contains valid data.</p>
</dd>

### -field <b>RestartableIPValid</b>

<dd>
<p>A single bit that indicates that the <b>RestartableIP</b> member contains valid data.</p>
</dd>

### -field <b>OverflowValid</b>

<dd>
<p>A single bit that indicates that the <b>Overflow</b> member contains valid data.</p>
</dd>

### -field <b>ParticipationValid</b>

<dd>
<p>A single bit that indicates that the <b>Participation</b> member contains valid data.</p>
</dd>

### -field <b>TimeoutValid</b>

<dd>
<p>A single bit that indicates that the <b>Timeout</b> member contains valid data.</p>
</dd>

### -field <b>AddressSpaceValid</b>

<dd>
<p>A single bit that indicates that the <b>AddressSpace</b> member contains valid data.</p>
</dd>

### -field <b>ReservedValid</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>TransactionType</b>

<dd>
<p>The type of transaction that was in progress when the error occurred. Possible values are:</p>
<p></p>
<dl>

### -field <a id="XPF_BUS_CHECK_TRANSACTIONTYPE_INSTRUCTION"></a><a id="xpf_bus_check_transactiontype_instruction"></a>XPF_BUS_CHECK_TRANSACTIONTYPE_INSTRUCTION

<dd>
<p>A processor instruction transaction.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_TRANSACTIONTYPE_DATAACCESS"></a><a id="xpf_bus_check_transactiontype_dataaccess"></a>XPF_BUS_CHECK_TRANSACTIONTYPE_DATAACCESS

<dd>
<p>A data access transaction.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_TRANSACTIONTYPE_GENERIC"></a><a id="xpf_bus_check_transactiontype_generic"></a>XPF_BUS_CHECK_TRANSACTIONTYPE_GENERIC

<dd>
<p>A generic transaction.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>TransactionTypeValid</b> bit is set.</p>
</dd>

### -field <b>Operation</b>

<dd>
<p>The type of bus operation that caused the error. Possible values are:</p>
<p></p>
<dl>

### -field <a id="XPF_BUS_CHECK_OPERATION_GENERIC"></a><a id="xpf_bus_check_operation_generic"></a>XPF_BUS_CHECK_OPERATION_GENERIC

<dd>
<p>The type of operation cannot be determined.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_OPERATION_GENREAD"></a><a id="xpf_bus_check_operation_genread"></a>XPF_BUS_CHECK_OPERATION_GENREAD

<dd>
<p>A generic read operation.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_OPERATION_GENWRITE"></a><a id="xpf_bus_check_operation_genwrite"></a>XPF_BUS_CHECK_OPERATION_GENWRITE

<dd>
<p>A generic write operation.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_OPERATION_DATAREAD"></a><a id="xpf_bus_check_operation_dataread"></a>XPF_BUS_CHECK_OPERATION_DATAREAD

<dd>
<p>A data read operation.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_OPERATION_DATAWRITE"></a><a id="xpf_bus_check_operation_datawrite"></a>XPF_BUS_CHECK_OPERATION_DATAWRITE

<dd>
<p>A data write operation.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_OPERATION_INSTRUCTIONFETCH"></a><a id="xpf_bus_check_operation_instructionfetch"></a>XPF_BUS_CHECK_OPERATION_INSTRUCTIONFETCH

<dd>
<p>An instruction fetch operation.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_OPERATION_PREFETCH"></a><a id="xpf_bus_check_operation_prefetch"></a>XPF_BUS_CHECK_OPERATION_PREFETCH

<dd>
<p>An instruction prefetch operation.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>OperationValid</b> bit is set.</p>
</dd>

### -field <b>Level</b>

<dd>
<p>The level of the bus hierarchy where the error occurred.</p>
<p>This member contains valid data only if the <b>LevelValid</b> bit is set.</p>
</dd>

### -field <b>ProcessorContextCorrupt</b>

<dd>
<p>A single bit that indicates that the processor context might have been corrupted.</p>
<p>This member contains valid data only if the <b>ProcessorContextCorruptValid</b> bit is set.</p>
</dd>

### -field <b>Uncorrected</b>

<dd>
<p>A single bit that indicates that the error has not been corrected.</p>
<p>This member contains valid data only if the <b>UncorrectedValid</b> bit is set.</p>
</dd>

### -field <b>PreciseIP</b>

<dd>
<p>A single bit that indicates that the instruction pointer that is specified in the <b>InstructionPointer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> structure that contains this WHEA_XPF_BUS_CHECK union is directly associated with the error.</p>
<p>This member contains valid data only if the <b>PreciseIPValid</b> bit is set.</p>
</dd>

### -field <b>RestartableIP</b>

<dd>
<p>A single bit that indicates that program execution can be restarted reliably at the instruction pointer that is specified in the <b>InstructionPointer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> union that contains this WHEA_XPF_BUS_CHECK structure.</p>
<p>This member contains valid data only if the <b>RestartableIPValid</b> bit is set.</p>
</dd>

### -field <b>Overflow</b>

<dd>
<p>A single bit that indicates that an error overflow occurred.</p>
<p>This member contains valid data only if the <b>OverflowValid</b> bit is set.</p>
</dd>

### -field <b>Participation</b>

<dd>
<p>The type of participation by the local processor. Possible values are:</p>
<p></p>
<dl>

### -field <a id="XPF_BUS_CHECK_PARTICIPATION_PROCORIGINATED"></a><a id="xpf_bus_check_participation_procoriginated"></a>XPF_BUS_CHECK_PARTICIPATION_PROCORIGINATED

<dd>
<p>The local processor originated the request.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_PARTICIPATION_PROCRESPONDED"></a><a id="xpf_bus_check_participation_procresponded"></a>XPF_BUS_CHECK_PARTICIPATION_PROCRESPONDED

<dd>
<p>The local processor responded to the request.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_PARTICIPATION_PROCOBSERVED"></a><a id="xpf_bus_check_participation_procobserved"></a>XPF_BUS_CHECK_PARTICIPATION_PROCOBSERVED

<dd>
<p>The local processor observed the request.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_PARTICIPATION_GENERIC"></a><a id="xpf_bus_check_participation_generic"></a>XPF_BUS_CHECK_PARTICIPATION_GENERIC

<dd>
<p>A generic value for this member if none of the other values are applicable.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>ParticipationValid</b> bit is set.</p>
</dd>

### -field <b>Timeout</b>

<dd>
<p>A single bit that indicates that a timeout occurred.</p>
<p>This member contains valid data only if the <b>TimeoutValid</b> bit is set.</p>
</dd>

### -field <b>AddressSpace</b>

<dd>
<p>The type of address space that was associated with the transaction that caused the error. Possible values are:</p>
<p></p>
<dl>

### -field <a id="XPF_BUS_CHECK_ADDRESS_MEMORY"></a><a id="xpf_bus_check_address_memory"></a>XPF_BUS_CHECK_ADDRESS_MEMORY

<dd>
<p>Memory address space.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_ADDRESS_RESERVED"></a><a id="xpf_bus_check_address_reserved"></a>XPF_BUS_CHECK_ADDRESS_RESERVED

<dd>
<p>Reserved.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_ADDRESS_IO"></a><a id="xpf_bus_check_address_io"></a>XPF_BUS_CHECK_ADDRESS_IO

<dd>
<p>I/O address space.</p>
</dd>

### -field <a id="XPF_BUS_CHECK_ADDRESS_OTHER"></a><a id="xpf_bus_check_address_other"></a>XPF_BUS_CHECK_ADDRESS_OTHER

<dd>
<p>An unclassified type of address space.</p>
</dd>
</dl>
<p>This member contains valid data only if the <b>AddressSpaceValid</b> bit is set.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>XpfBusCheck</b>

<dd>
<p>A ULONGLONG representation of the contents of the WHEA_XPF_BUS_CHECK union.</p>
</dd>
</dl>

## -remarks
<p>If the <b>CheckInfoId</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> structure contains WHEA_BUSCHECK_GUID, the <b>CheckInfo</b> member of the WHEA_XPF_PROCINFO structure contains a WHEA_XPF_BUS_CHECK union.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_BUS_CHECK union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
