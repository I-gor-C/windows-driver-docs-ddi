---
UID: NS.ntddk._WHEA_PROCESSOR_FAMILY_INFO
title: WHEA_PROCESSOR_FAMILY_INFO
author: windows-driver-content
description: The WHEA_PROCESSOR_FAMILY_INFO union describes the processor family information for an x86 or x64 processor.
old-location: whea\whea_processor_family_info.htm
ms.assetid: cc20c2d6-c76b-4f72-9762-23b9aa5fe946
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
req.alt-api: WHEA_PROCESSOR_FAMILY_INFO
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
ms.keywords: WHEA_PROCESSOR_FAMILY_INFO, WHEA_PROCESSOR_FAMILY_INFO, *PWHEA_PROCESSOR_FAMILY_INFO
req.iface: 
---

# WHEA_PROCESSOR_FAMILY_INFO structure



## -description
<p>The WHEA_PROCESSOR_FAMILY_INFO union describes the processor family information for an x86 or x64 processor.</p>


## -syntax

````
typedef union _WHEA_PROCESSOR_FAMILY_INFO {
  struct {
    ULONG Stepping  :4;
    ULONG Model  :4;
    ULONG Family  :4;
    ULONG ProcessorType  :2;
    ULONG Reserved1  :2;
    ULONG ExtendedModel  :4;
    ULONG ExtendedFamily  :8;
    ULONG Reserved2  :4;
    ULONG Reserved3;
  };
  ULONGLONG AsULONGLONG;
} WHEA_PROCESSOR_FAMILY_INFO, *PWHEA_PROCESSOR_FAMILY_INFO;
````


## -struct-fields
<dl>

### -field <b>Stepping</b>

<dd>
<p>The stepping of the processor.</p>
</dd>

### -field <b>Model</b>

<dd>
<p>The processor model identifier.</p>
</dd>

### -field <b>Family</b>

<dd>
<p>The processor family identifier.</p>
</dd>

### -field <b>ProcessorType</b>

<dd>
<p>The processor type identifier.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>ExtendedModel</b>

<dd>
<p>The extended processor model identifier.</p>
</dd>

### -field <b>ExtendedFamily</b>

<dd>
<p>The extended processor family identifier.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>AsULONGLONG</b>

<dd>
<p>A ULONGLONG representation of the contents of the WHEA_PROCESSOR_FAMILY_INFO union.</p>
</dd>
</dl>

## -remarks
<p>For x86 and x64 processors, the <b>CPUVersion</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560607">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure contains a WHEA_PROCESSOR_FAMILY_INFO union.</p>

<p>The contents of this union are obtained by executing the CPUID instruction with the EAX register set to 1 on input. For more information about the CPUID instruction, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>. For additional information about the data that is contained in the members of this union, see <a href="http://go.microsoft.com/fwlink/p/?linkid=80097">AP-485 Intel Processor Identification and the CPUID Instruction</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560607">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PROCESSOR_FAMILY_INFO union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
