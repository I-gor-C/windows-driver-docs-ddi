---
UID: NS.ntddk._WHEA_XPF_MS_CHECK
title: WHEA_XPF_MS_CHECK
author: windows-driver-content
description: The WHEA_XPF_MS_CHECK union describes microarchitecture-specific error information for an x86 or x64 processor.
old-location: whea\whea_xpf_ms_check.htm
ms.assetid: aa446b31-ac53-4623-bacd-72ab72e94618
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
req.alt-api: WHEA_XPF_MS_CHECK
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
ms.keywords: WHEA_XPF_MS_CHECK, WHEA_XPF_MS_CHECK, *PWHEA_XPF_MS_CHECK
req.iface: 
---

# WHEA_XPF_MS_CHECK structure



## -description
<p>The WHEA_XPF_MS_CHECK union describes microarchitecture-specific error information for an x86 or x64 processor.</p>


## -syntax

````
typedef union _WHEA_XPF_MS_CHECK {
  struct {
    ULONGLONG ErrorTypeValid  :1;
    ULONGLONG ProcessorContextCorruptValid  :1;
    ULONGLONG UncorrectedValid  :1;
    ULONGLONG PreciseIPValid  :1;
    ULONGLONG RestartableIPValid  :1;
    ULONGLONG OverflowValid  :1;
    ULONGLONG ReservedValid  :10;
    ULONGLONG ErrorType  :3;
    ULONGLONG ProcessorContextCorrupt  :1;
    ULONGLONG Uncorrected  :1;
    ULONGLONG PreciseIP  :1;
    ULONGLONG RestartableIP  :1;
    ULONGLONG Overflow  :1;
    ULONGLONG Reserved  :40;
  };
  ULONGLONG XpfMsCheck;
} WHEA_XPF_MS_CHECK, *PWHEA_XPF_MS_CHECK;
````


## -struct-fields
<dl>

### -field <b>ErrorTypeValid</b>

<dd>
<p>A single bit that indicates that the <b>ErrorType</b> member contains valid data.</p>
</dd>

### -field <b>ProcessorContextCorruptValid</b>

<dd>
<p>A single bit that indicates that the <b>ProcessorContextCorrupt</b> member contains valid data.</p>
</dd>

### -field <b>UncorrectedValid</b>

<dd>
<p>A single bit that indicates that the <b>Uncorrected</b> member contains valid data.</p>
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

### -field <b>ReservedValid</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>ErrorType</b>

<dd>
<p>The type of error that occurred. Possible values are:</p>
<p></p>
<dl>

### -field <a id="XPF_MS_CHECK_ERRORTYPE_NOERROR"></a><a id="xpf_ms_check_errortype_noerror"></a>XPF_MS_CHECK_ERRORTYPE_NOERROR

<dd>
<p>No error occurred.</p>
</dd>

### -field <a id="XPF_MS_CHECK_ERRORTYPE_UNCLASSIFIED"></a><a id="xpf_ms_check_errortype_unclassified"></a>XPF_MS_CHECK_ERRORTYPE_UNCLASSIFIED

<dd>
<p>An unclassified error.</p>
</dd>

### -field <a id="XPF_MS_CHECK_ERRORTYPE_MCROMPARITY"></a><a id="xpf_ms_check_errortype_mcromparity"></a>XPF_MS_CHECK_ERRORTYPE_MCROMPARITY

<dd>
<p>A microcode ROM parity error.</p>
</dd>

### -field <a id="XPF_MS_CHECK_ERRORTYPE_EXTERNAL"></a><a id="xpf_ms_check_errortype_external"></a>XPF_MS_CHECK_ERRORTYPE_EXTERNAL

<dd>
<p>An external error.</p>
</dd>

### -field <a id="XPF_MS_CHECK_ERRORTYPE_FRC"></a><a id="xpf_ms_check_errortype_frc"></a>XPF_MS_CHECK_ERRORTYPE_FRC

<dd>
<p>A functional redundancy checking (FRC) error.</p>
</dd>

### -field <a id="XPF_MS_CHECK_ERRORTYPE_INTERNALUNCLASSIFIED"></a><a id="xpf_ms_check_errortype_internalunclassified"></a>XPF_MS_CHECK_ERRORTYPE_INTERNALUNCLASSIFIED

<dd>
<p>An unclassified internal error.</p>
</dd>
</dl>
<p>All other values are processor-specific.</p>
<p>This member contains valid data only if the <b>ErrorTypeValid</b> bit is set.</p>
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
<p>A single bit that indicates that the instruction pointer that is specified in the <b>InstructionPointer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> structure that contains this WHEA_XPF_MS_CHECK union is directly associated with the error.</p>
<p>This member contains valid data only if the <b>PreciseIPValid </b>bit is set.</p>
</dd>

### -field <b>RestartableIP</b>

<dd>
<p>A single bit that indicates that program execution can be restarted reliably at the instruction pointer that is specified in the <b>InstructionPointer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> union that contains this WHEA_XPF_MS_CHECK structure.</p>
<p>This member contains valid data only if the <b>RestartableIPValid</b> bit is set.</p>
</dd>

### -field <b>Overflow</b>

<dd>
<p>A single bit that indicates that an error overflow occurred.</p>
<p>This member contains valid data only if the <b>OverflowValid</b> bit is set.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>XpfMsCheck</b>

<dd>
<p>A ULONGLONG representation of the contents of the WHEA_XPF_MS_CHECK union.</p>
</dd>
</dl>

## -remarks
<p>If the <b>CheckInfoId</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560661">WHEA_XPF_PROCINFO</a> structure contains WHEA_MSCHECK_GUID, the <b>CheckInfo</b> member of the WHEA_XPF_PROCINFO structure contains a WHEA_XPF_MS_CHECK union.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_MS_CHECK union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
