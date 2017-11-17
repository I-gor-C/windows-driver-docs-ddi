---
UID: NS.ntddk._WHEA_PROCESSOR_GENERIC_ERROR_SECTION
title: WHEA_PROCESSOR_GENERIC_ERROR_SECTION
author: windows-driver-content
description: Describes processor error data that is not specific to a particular processor architecture.
old-location: whea\whea_processor_generic_error_section.htm
ms.assetid: d1ac2ca0-ad08-4149-b489-53807f308fc0
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_PROCESSOR_GENERIC_ERROR_SECTION
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
ms.keywords: WHEA_PROCESSOR_GENERIC_ERROR_SECTION, WHEA_PROCESSOR_GENERIC_ERROR_SECTION, *PWHEA_PROCESSOR_GENERIC_ERROR_SECTION
req.iface: 
---

# WHEA_PROCESSOR_GENERIC_ERROR_SECTION structure



## -description
<p>The 
   <b>WHEA_PROCESSOR_GENERIC_ERROR_SECTION</b> 
   structure describes processor error data that is not specific to a particular processor architecture.</p>


## -syntax

````
typedef struct _WHEA_PROCESSOR_GENERIC_ERROR_SECTION {
  WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS ValidBits;
  UCHAR                                          ProcessorType;
  UCHAR                                          InstructionSet;
  UCHAR                                          ErrorType;
  UCHAR                                          Operation;
  UCHAR                                          Flags;
  UCHAR                                          Level;
  USHORT                                         Reserved;
  ULONGLONG                                      CPUVersion;
  UCHAR                                          CPUBrandString[128];
  ULONGLONG                                      ProcessorId;
  ULONGLONG                                      TargetAddress;
  ULONGLONG                                      RequesterId;
  ULONGLONG                                      ResponderId;
  ULONGLONG                                      InstructionPointer;
} WHEA_PROCESSOR_GENERIC_ERROR_SECTION, *PWHEA_PROCESSOR_GENERIC_ERROR_SECTION;
````


## -struct-fields
<dl>

### -field <b>ValidBits</b>

<dd>
<p>A 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff560610">WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS</a> 
      union that specifies which members of this structure contain valid data.</p>
</dd>

### -field <b>ProcessorType</b>

<dd>
<p>The processor architecture of the processor.</p>
<p>This member contains valid data only if the 
       <b>ProcessorType</b> bit of the <b>ValidBits</b> member is set.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCTYPE_XPF"></a><a id="genproc_proctype_xpf"></a><dl>

### -field <b>GENPROC_PROCTYPE_XPF</b>

</dl>
</td>
<td width="60%">
<p>x86/x64 processor family</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCTYPE_IPF"></a><a id="genproc_proctype_ipf"></a><dl>

### -field <b>GENPROC_PROCTYPE_IPF</b>

</dl>
</td>
<td width="60%">
<p>Intel Itanium processor family</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>InstructionSet</b>

<dd>
<p>The instruction set that was executing when the error occurred.</p>
<p>This member contains valid data only if the <b>InstructionSet</b> bit of the 
       <b>ValidBits</b> member is set.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCISA_X86"></a><a id="genproc_procisa_x86"></a><dl>

### -field <b>GENPROC_PROCISA_X86</b>

</dl>
</td>
<td width="60%">
<p>x86</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCISA_IPF"></a><a id="genproc_procisa_ipf"></a><dl>

### -field <b>GENPROC_PROCISA_IPF</b>

</dl>
</td>
<td width="60%">
<p>Itanium</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCISA_X64"></a><a id="genproc_procisa_x64"></a><dl>

### -field <b>GENPROC_PROCISA_X64</b>

</dl>
</td>
<td width="60%">
<p>x64</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ErrorType</b>

<dd>
<p>The type of error that occurred.</p>
<p>This member contains valid data only if the <b>ErrorType</b> bit of the 
       <b>ValidBits</b> member is set.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCERRTYPE_UNKNOWN"></a><a id="genproc_procerrtype_unknown"></a><dl>

### -field <b>GENPROC_PROCERRTYPE_UNKNOWN</b>

</dl>
</td>
<td width="60%">
<p>Unknown error</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCERRTYPE_CACHE"></a><a id="genproc_procerrtype_cache"></a><dl>

### -field <b>GENPROC_PROCERRTYPE_CACHE</b>

</dl>
</td>
<td width="60%">
<p>Cache error</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCERRTYPE_TLB"></a><a id="genproc_procerrtype_tlb"></a><dl>

### -field <b>GENPROC_PROCERRTYPE_TLB</b>

</dl>
</td>
<td width="60%">
<p>Translation lookaside buffer error</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCERRTYPE_BUS"></a><a id="genproc_procerrtype_bus"></a><dl>

### -field <b>GENPROC_PROCERRTYPE_BUS</b>

</dl>
</td>
<td width="60%">
<p>Bus error</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_PROCERRTYPE_MAE"></a><a id="genproc_procerrtype_mae"></a><dl>

### -field <b>GENPROC_PROCERRTYPE_MAE</b>

</dl>
</td>
<td width="60%">
<p>Microarchitecture error</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Operation</b>

<dd>
<p>The type of operation that was executing when the error occurred.</p>
<p>This member contains valid data only if the <b>Operation</b> bit of the 
       <b>ValidBits</b> member is set.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="GENPROC_OP_GENERIC"></a><a id="genproc_op_generic"></a><dl>

### -field <b>GENPROC_OP_GENERIC</b>

</dl>
</td>
<td width="60%">
<p>Unknown or generic operation</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_OP_DATAREAD"></a><a id="genproc_op_dataread"></a><dl>

### -field <b>GENPROC_OP_DATAREAD</b>

</dl>
</td>
<td width="60%">
<p>Data read</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_OP_DATAWRITE"></a><a id="genproc_op_datawrite"></a><dl>

### -field <b>GENPROC_OP_DATAWRITE</b>

</dl>
</td>
<td width="60%">
<p>Data write</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_OP_INSTRUCTIONEXE"></a><a id="genproc_op_instructionexe"></a><dl>

### -field <b>GENPROC_OP_INSTRUCTIONEXE</b>

</dl>
</td>
<td width="60%">
<p>Instruction execution</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bit-wise OR'ed combination of flags that provides additional information about the error.</p>
<p>This member contains valid data only if the <b>Flags</b> bit of the 
       <b>ValidBits</b> member is set.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="GENPROC_FLAGS_RESTARTABLE"></a><a id="genproc_flags_restartable"></a><dl>

### -field <b>GENPROC_FLAGS_RESTARTABLE</b>

</dl>
</td>
<td width="60%">
<p>Program execution can be restarted reliably after the error.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_FLAGS_PRECISEIP"></a><a id="genproc_flags_preciseip"></a><dl>

### -field <b>GENPROC_FLAGS_PRECISEIP</b>

</dl>
</td>
<td width="60%">
<p>The instruction pointer in the <b>InstructionPointer</b> member is directly 
        associated with the error.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_FLAGS_OVERFLOW"></a><a id="genproc_flags_overflow"></a><dl>

### -field <b>GENPROC_FLAGS_OVERFLOW</b>

</dl>
</td>
<td width="60%">
<p>A machine check overflow occurred. This happens when a second error occurs while the results of the 
        previous error are still in the error reporting resources.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="GENPROC_FLAGS_CORRECTED"></a><a id="genproc_flags_corrected"></a><dl>

### -field <b>GENPROC_FLAGS_CORRECTED</b>

</dl>
</td>
<td width="60%">
<p>The error was corrected by the hardware or the firmware.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Level</b>

<dd>
<p>The level of the structure where the error occurred, with zero being the lowest level of cache.</p>
<p>This member contains valid data only if the <b>Level</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>CPUVersion</b>

<dd>
<p>The CPU version, which includes the family, model, and stepping information.</p>
<ul>
<li>For x86 and x64 processors, this member contains a 
        <a href="https://msdn.microsoft.com/library/windows/hardware/ff560605">WHEA_PROCESSOR_FAMILY_INFO</a> union.</li>
<li>For Itanium processors, this member contains the data provided in CPUID Register 3.</li>
</ul>
<p>This member contains valid data only if the <b>CPUVersion</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>CPUBrandString</b>

<dd>
<p>The CPU brand string.</p>
<ul>
<li>For x86 and x64 processors, this member contains the result of executing the CPUID instruction with EAX 
        set to 0x80000002 on input, followed by executing the CPUID instruction with EAX set to 0x80000003 on input. 
        For more information about the CPUID instruction, see the 
        <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.</li>
<li>For Itanium processors, this member contains the result of executing the 
        <b>PAL_BRAND_INFO</b> procedure.</li>
</ul>
<p>This member contains valid data only if the <b>CpuBrandString</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>ProcessorId</b>

<dd>
<p>An identifier that uniquely identifies the logical processor in the system.</p>
<ul>
<li>For x86 and x64 processors, this member contains the value programmed into the local APIC ID 
        register.</li>
<li>For Itanium processors, this member contains the value programmed into the LID register.</li>
</ul>
<p>This member contains valid data only if the <b>ProcessorId</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>TargetAddress</b>

<dd>
<p>The target address associated with the error.</p>
<p>This member contains valid data only if the <b>TargetAddress</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>RequesterId</b>

<dd>
<p>An identifier that uniquely identifies the requester associated with the error.</p>
<p>This member contains valid data only if the <b>RequesterId</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>ResponderId</b>

<dd>
<p>An identifier that uniquely identifies the responder associated with the error.</p>
<p>This member contains valid data only if the <b>ResponderId</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>

### -field <b>InstructionPointer</b>

<dd>
<p>The instruction pointer at the time that the error occurred.</p>
<p>This member contains valid data only if the <b>InstructionPointer</b> bit of the 
       <b>ValidBits</b> member is set.</p>
</dd>
</dl>

## -remarks
<p>The 
     <b>WHEA_PROCESSOR_GENERIC_ERROR_SECTION</b> 
     structure describes the error data that is contained in a generic processor error section of an 
     <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>. An error record contains a generic processor 
     error section only if the <b>SectionType</b> member of one of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> 
     structures that describe the error record sections for that error record contains 
     <b>PROCESSOR_GENERIC_ERROR_SECTION_GUID</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560610">WHEA_PROCESSOR_GENERIC_ERROR_SECTION_VALIDBITS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560605">WHEA_PROCESSOR_FAMILY_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PROCESSOR_GENERIC_ERROR_SECTION structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
