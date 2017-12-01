---
UID: NS.ntddk._WHEA_ERROR_RECORD_HEADER
title: WHEA_ERROR_RECORD_HEADER
author: windows-driver-content
description: The WHEA_ERROR_RECORD_HEADER structure describes general information about a hardware error condition.
old-location: whea\whea_error_record_header.htm
old-project: whea
ms.assetid: 2e6476c7-d096-4756-bebb-56fe559dce6d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_ERROR_RECORD_HEADER, WHEA_ERROR_RECORD_HEADER, *PWHEA_ERROR_RECORD_HEADER
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
req.alt-api: WHEA_ERROR_RECORD_HEADER
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

# WHEA_ERROR_RECORD_HEADER structure



## -description
<p>The WHEA_ERROR_RECORD_HEADER structure describes general information about a hardware error condition.</p>


## -syntax

````
typedef struct _WHEA_ERROR_RECORD_HEADER {
  ULONG                              Signature;
  WHEA_REVISION                      Revision;
  ULONG                              SignatureEnd;
  USHORT                             SectionCount;
  WHEA_ERROR_SEVERITY                Severity;
  WHEA_ERROR_RECORD_HEADER_VALIDBITS ValidBits;
  ULONG                              Length;
  WHEA_TIMESTAMP                     Timestamp;
  GUID                               PlatformId;
  GUID                               PartitionId;
  GUID                               CreatorId;
  GUID                               NotifyType;
  ULONGLONG                          RecordId;
  WHEA_ERROR_RECORD_HEADER_FLAGS     Flags;
  WHEA_PERSISTENCE_INFO              PersistenceInfo;
  UCHAR                              Reserved[12];
} WHEA_ERROR_RECORD_HEADER, *PWHEA_ERROR_RECORD_HEADER;
````


## -struct-fields
<dl>

### -field <b>Signature</b>

<dd>
<p>The signature of the error record. This member contains the value 'REPC'.</p>
</dd>

### -field <b>Revision</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-revision.md">WHEA_REVISION</a> union that describes the revision level of the WHEA_ERROR_RECORD_HEADER structure.</p>
</dd>

### -field <b>SignatureEnd</b>

<dd>
<p>The end of the signature of the error record. This member contains the value 0xFFFFFFFF.</p>
</dd>

### -field <b>SectionCount</b>

<dd>
<p>The number of sections of error information that are contained in the error record.</p>
</dd>

### -field <b>Severity</b>

<dd>
<p>A <a href="..\ntddk\ne-ntddk--whea-error-severity.md">WHEA_ERROR_SEVERITY</a>-typed value that indicates the severity of the error condition described by the error record.</p>
</dd>

### -field <b>ValidBits</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-error-record-header-validbits.md">WHEA_ERROR_RECORD_HEADER_VALIDBITS</a> union that specifies which members of the WHEA_ERROR_RECORD_HEADER structure contain valid data.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of the error record.</p>
</dd>

### -field <b>Timestamp</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-timestamp.md">WHEA_TIMESTAMP</a> union that indicates the time that the error was reported to the operating system. This member contains valid data only if the <b>ValidBits.Timestamp</b> bit is set.</p>
</dd>

### -field <b>PlatformId</b>

<dd>
<p>A GUID that identifies the platform on which the hardware error occurred. This member contains valid data only if the <b>ValidBits.PlatformId</b> bit is set.</p>
</dd>

### -field <b>PartitionId</b>

<dd>
<p>A GUID that identifies the partition on which the hardware error occurred. This member contains valid data only if the <b>ValidBits.PartitionId</b> bit is set.</p>
</dd>

### -field <b>CreatorId</b>

<dd>
<p>A GUID that identifies the entity that created the error record. When the Windows kernel creates an error record, it sets this member to WHEA_RECORD_CREATOR_GUID.</p>
</dd>

### -field <b>NotifyType</b>

<dd>
<p>A GUID that identifies the notification mechanism by which an error condition is reported to the operating system. The following are the GUIDs for the standard notification types:</p>
<p></p>
<dl>

### -field <a id="CMC_NOTIFY_TYPE_GUID"></a><a id="cmc_notify_type_guid"></a>CMC_NOTIFY_TYPE_GUID

<dd>
<p>Corrected Machine Check (CMC)</p>
</dd>

### -field <a id="CPE_NOTIFY_TYPE_GUID"></a><a id="cpe_notify_type_guid"></a>CPE_NOTIFY_TYPE_GUID

<dd>
<p>Corrected Platform Error (CPE)</p>
</dd>

### -field <a id="MCE_NOTIFY_TYPE_GUID"></a><a id="mce_notify_type_guid"></a>MCE_NOTIFY_TYPE_GUID

<dd>
<p>Machine Check Exception (MCE)</p>
</dd>

### -field <a id="PCIe_NOTIFY_TYPE_GUID"></a><a id="pcie_notify_type_guid"></a><a id="PCIE_NOTIFY_TYPE_GUID"></a>PCIe_NOTIFY_TYPE_GUID

<dd>
<p>PCI Express (PCIe) Error</p>
</dd>

### -field <a id="INIT_NOTIFY_TYPE_GUID"></a><a id="init_notify_type_guid"></a>INIT_NOTIFY_TYPE_GUID

<dd>
<p>INIT Error Record (INIT)</p>
</dd>

### -field <a id="NMI_NOTIFY_TYPE_GUID"></a><a id="nmi_notify_type_guid"></a>NMI_NOTIFY_TYPE_GUID

<dd>
<p>Nonmaskable Interrupt (NMI)</p>
</dd>

### -field <a id="BOOT_NOTIFY_TYPE_GUID"></a><a id="boot_notify_type_guid"></a>BOOT_NOTIFY_TYPE_GUID

<dd>
<p>Boot Error Record (BOOT)</p>
</dd>
</dl>
<p>For error notification types that do not conform to one of the standard types in the previous list, a platform-specific GUID can be defined to identify the notification mechanism. If the notification type does not correspond to any of the standard notification types or any platform-specific notification types, this member is set to GENERIC_NOTIFY_TYPE_GUID.</p>
</dd>

### -field <b>RecordId</b>

<dd>
<p>The identifier of the error record. This identifier is unique only on the system that created the error record.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A WHEA_ERROR_RECORD_HEADER_FLAGS union that describes the error condition. The WHEA_ERROR_RECORD_HEADER_FLAGS union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_ERROR_RECORD_HEADER_FLAGS {
  struct {
    ULONG  Recovered:1;
    ULONG  PreviousError:1;
    ULONG  Simulated:1;
    ULONG  Reserved:29;
  };
  ULONG  AsULONG;
} WHEA_ERROR_RECORD_HEADER_FLAGS, *PWHEA_ERROR_RECORD_HEADER_FLAGS;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="Recovered"></a><a id="recovered"></a><a id="RECOVERED"></a><b>Recovered</b>

<dd>
<p>A single bit that indicates that the operating system recovered from the error condition.</p>
</dd>

### -field <a id="PreviousError"></a><a id="previouserror"></a><a id="PREVIOUSERROR"></a><b>PreviousError</b>

<dd>
<p>A single bit that indicates that the error condition occurred in a previous session of the operating system.</p>
</dd>

### -field <a id="Simulated"></a><a id="simulated"></a><a id="SIMULATED"></a><b>Simulated</b>

<dd>
<p>A single bit that indicates that the error condition was simulated.</p>
</dd>

### -field <a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="AsULONG"></a><a id="asulong"></a><a id="ASULONG"></a><b>AsULONG</b>

<dd>
<p>A ULONG representation of the contents of the WHEA_ERROR_RECORD_HEADER_FLAGS union.</p>
</dd>
</dl>
</dd>

### -field <b>PersistenceInfo</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-persistence-info.md">WHEA_PERSISTENCE_INFO</a> union that is used by the error record persistence interface.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_ERROR_RECORD_HEADER structure is contained within the <a href="..\ntddk\ns-ntddk--whea-error-record.md">WHEA_ERROR_RECORD</a> structure. The WHEA_ERROR_RECORD_HEADER structure describes general information about the hardware error condition that is described by the error record.</p>

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
<a href="..\ntddk\ns-ntddk--whea-error-record.md">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-error-record-header-validbits.md">WHEA_ERROR_RECORD_HEADER_VALIDBITS</a>
</dt>
<dt>
<a href="..\ntddk\ne-ntddk--whea-error-severity.md">WHEA_ERROR_SEVERITY</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-persistence-info.md">WHEA_PERSISTENCE_INFO</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-revision.md">WHEA_REVISION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-timestamp.md">WHEA_TIMESTAMP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_RECORD_HEADER structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
