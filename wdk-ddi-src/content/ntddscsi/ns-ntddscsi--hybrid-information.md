---
UID: NS.ntddscsi._HYBRID_INFORMATION
title: HYBRID_INFORMATION
author: windows-driver-content
description: The HYBRID_INFORMATION structure contains hybrid disk capability information.
old-location: storage\hybrid_information.htm
old-project: storage
ms.assetid: 5CD8E422-8CEE-43E8-9703-520FDBE6BF5E
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HYBRID_INFORMATION, HYBRID_INFORMATION, *PHYBRID_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddscsi.h
req.include-header: Ntddscsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HYBRID_INFORMATION
req.alt-loc: Ntddscsi.h
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
---

# HYBRID_INFORMATION structure



## -description
<p>The <b>HYBRID_INFORMATION</b> structure contains hybrid disk capability information. The structure is returned when the HYBRID_FUNCTION_GET_INFO function is selected in a <a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-miniport-hybrid.md">IOCTL_SCSI_MINIPORT_HYBRID</a> request  sent to an HBA miniport driver.</p>


## -syntax

````
typedef struct _HYBRID_INFORMATION {
  ULONG          Version;
  ULONG          Size;
  BOOLEAN        HybridSupported;
  NVCACHE_STATUS Status;
  NVCACHE_TYPE   CacheTypeEffective;
  NVCACHE_TYPE   CacheTypeDefault;
  ULONG          FractionBase;
  ULONGLONG      CacheSize;
  struct {
    ULONG WriteCacheChangeable  :1;
    ULONG WriteThroughIoSupported  :1;
    ULONG FlushCacheSupported  :1;
    ULONG Removable  :1;
    ULONG ReservedBits  :28;
  } Attributes;
  struct {
    UCHAR                             PriorityLevelCount;
    BOOLEAN                           MaxPriorityBehavior;
    ULONG                             DirtyThresholdLow;
    ULONG                             DirtyThresholdHigh;
    struct {
      ULONG CacheDisable  :1;
      ULONG SetDirtyThreshold  :1;
      ULONG PriorityDemoteBySize  :1;
      ULONG PriorityChangeByLbaRange  :1;
      ULONG Evict  :1;
      ULONG ReservedBits  :27;
      ULONG MaxEvictCommands;
      ULONG MaxLbaRangeCountForEvict;
      ULONG MaxLbaRangeCountForChangeLba;
    } SupportedCommands;
    NVCACHE_PRIORITY_LEVEL_DESCRIPTOR Priority[];
  } Priorities;
} HYBRID_INFORMATION, *PHYBRID_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. Set to HYBRID_REQUEST_INFO_STRUCTURE_VERSION.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure. Set to <b>sizeof</b>(HYBRID_INFORMATION).</p>
</dd>

### -field <b>HybridSupported</b>

<dd>
<p>Miniport supports for hybrid disks. Set to <b>TRUE</b> if hybrid disks are supported. Otherwise, <b>FALSE</b>.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>The status of the hybrid disk cache. This contains one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NvCacheStatusUnknown"></a><a id="nvcachestatusunknown"></a><a id="NVCACHESTATUSUNKNOWN"></a><dl>

### -field <b>NvCacheStatusUnknown</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver is not able to report the cache status.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NvCacheStatusDisabling"></a><a id="nvcachestatusdisabling"></a><a id="NVCACHESTATUSDISABLING"></a><dl>

### -field <b>NvCacheStatusDisabling</b>

</dl>
</td>
<td width="60%">
<p>The cache is currently changing to <b>NvCacheStatusDisabled</b> status.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NvCacheStatusDisabled"></a><a id="nvcachestatusdisabled"></a><a id="NVCACHESTATUSDISABLED"></a><dl>

### -field <b>NvCacheStatusDisabled</b>

</dl>
</td>
<td width="60%">
<p>The cache on the hybrid disk is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NvCacheStatusEnabled"></a><a id="nvcachestatusenabled"></a><a id="NVCACHESTATUSENABLED"></a><dl>

### -field <b>NvCacheStatusEnabled</b>

</dl>
</td>
<td width="60%">
<p>The cache on the hybrid disk is enabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CacheTypeEffective</b>

<dd>
<p>The non-volatile caching type currently set for hybrid disk. The effective cache type is one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NvCacheTypeUnknown"></a><a id="nvcachetypeunknown"></a><a id="NVCACHETYPEUNKNOWN"></a><dl>

### -field <b>NvCacheTypeUnknown</b>

</dl>
</td>
<td width="60%">
<p>The miniport driver is not able to report the cache type</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NvCacheNone"></a><a id="nvcachenone"></a><a id="NVCACHENONE"></a><dl>

### -field <b>NvCacheNone</b>

</dl>
</td>
<td width="60%">
<p>The disk does not support a non-volatile cache.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NvCacheTypeWriteBack"></a><a id="nvcachetypewriteback"></a><a id="NVCACHETYPEWRITEBACK"></a><dl>

### -field <b>NvCacheTypeWriteBack</b>

</dl>
</td>
<td width="60%">
<p>Write-back caching is supported by hybrid disk.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NvCacheTypeWriteThrough"></a><a id="nvcachetypewritethrough"></a><a id="NVCACHETYPEWRITETHROUGH"></a><dl>

### -field <b>NvCacheTypeWriteThrough</b>

</dl>
</td>
<td width="60%">
<p>Write-through caching is supported by hybrid disk.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CacheTypeDefault</b>

<dd>
<p>The default caching type used by the hybrid disk. The possible values are the same as for <b>CacheTypeEffective</b>.</p>
</dd>

### -field <b>FractionBase</b>

<dd>
<p>The base value for fractional fields in this structure. This value is set to 255.</p>
</dd>

### -field <b>CacheSize</b>

<dd>
<p>The size, in LBAs, of the non-volatile on the hybrid disk.</p>
</dd>

### -field <b>Attributes</b>

<dd>
<p>The hybrid disk attributes.</p>
<dl>

### -field <b>WriteCacheChangeable</b>

<dd>
<p>Support for changes in write caching policy. The value is 1 policy changes are allowed. Otherwise, changes are ignored.</p>
</dd>

### -field <b>WriteThroughIoSupported</b>

<dd>
<p>Support for individual write operations when write-through caching is used. The value is 1 if individual writes are supported. Otherwise, the values is 0.</p>
</dd>

### -field <b>FlushCacheSupported</b>

<dd>
<p>Support for non-volatile cache flush. The value is 1 if flushes are supported. Otherwise, the value is 0.</p>
</dd>

### -field <b>Removable</b>

<dd>
<p>Support of removal of the non-volatile cache from the disk. The value is 1 if the cache is removable. Otherwise, the value is 0.</p>
</dd>

### -field <b>ReservedBits</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>Priorities</b>

<dd>
<p>Priority settings for the hybrid disk.</p>
<dl>

### -field <b>PriorityLevelCount</b>

<dd>
<p>The number of priority levels supported by the cache. Currently, a non-zero value indicates support for all priorities.</p>
</dd>

### -field <b>MaxPriorityBehavior</b>

<dd>
<p>If <b>TRUE</b>, the disk I/O can fail at maximum priority if the cache is full.  Otherwise, if <b>FALSE</b>, the operation will complete to disk.</p>
</dd>

### -field <b>DirtyThresholdLow</b>

<dd>
<p>The low threshold for a cache flush. This value is ratio in the range of <b>FractionBase</b>.</p>
</dd>

### -field <b>DirtyThresholdHigh</b>

<dd>
<p>The low threshold for a cache flush. This value is ratio in the range of <b>FractionBase</b>.</p>
</dd>

### -field <b>SupportedCommands</b>

<dd>
<p>Support for non-volatile cache specific commands to the hybrid disk.</p>
<dl>

### -field <b>CacheDisable</b>

<dd>
<p>Support for changes in write caching policy. The value is 1 policy changes are allowed. Otherwise, changes are ignored.</p>
</dd>

### -field <b>SetDirtyThreshold</b>

<dd>
<p>Support for individual write operations when write-through caching is used. The value is 1 if individual writes are supported. Otherwise, the values is 0.</p>
</dd>

### -field <b>PriorityDemoteBySize</b>

<dd>
<p>Support for non-volatile cache flush. The value is 1 if flushes are supported. Otherwise, the value is 0.</p>
</dd>

### -field <b>PriorityChangeByLbaRange</b>

<dd>
<p>Support for LBA range priority changes. The value is 1 if priority changes  are supported. Otherwise, the value is 0.</p>
</dd>

### -field <b>Evict</b>

<dd>
<p>Support of removal of the non-volatile cache from the disk. The value is 1 if the cache is removable. Otherwise, the value is 0.</p>
</dd>

### -field <b>ReservedBits</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>MaxEvictCommands</b>

<dd>
<p>The maximum concurrent Evict commands allowed that are outstanding. This value is valid when <b>Evict</b> is set to 1.</p>
</dd>

### -field <b>MaxLbaRangeCountForEvict</b>

<dd>
<p>The maximum number of LBA ranges possible to associate with an Evict command. This value is valid when <b>Evict</b> is set to 1.</p>
</dd>

### -field <b>MaxLbaRangeCountForChangeLba</b>

<dd>
<p>The maximum number of LBA ranges possible to associate with a Priority Change command. This value is valid when <b>PriorityChangeByLbaRange</b> is set to 1.</p>
</dd>
</dl>
</dd>

### -field <b>Priority</b>

<dd>
<p>An array of priority level descriptors. The number of descriptors present in the array is set in <b>PriorityLevelCount</b>.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddscsi.h (include Ntddscsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-miniport-hybrid.md">IOCTL_SCSI_MINIPORT_HYBRID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HYBRID_INFORMATION structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
