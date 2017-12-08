---
UID: NS.wdm._PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK
title: PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK
author: windows-driver-content
description: The PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure describes a PCI Express (PCIe) secondary uncorrectable error mask register of a PCIe advanced error reporting capability structure.
old-location: pci\pci_express_sec_uncorrectable_error_mask.htm
old-project: PCI
ms.assetid: 99387bcc-301d-4406-bcff-fb5569c88c90
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Ntddk.h, Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure



## -description
<p>The PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure describes a PCI Express (PCIe) secondary uncorrectable error mask register of a PCIe advanced error reporting capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK {
  struct {
    ULONG TargetAbortOnSplitCompletion  :1;
    ULONG MasterAbortOnSplitCompletion  :1;
    ULONG ReceivedTargetAbort  :1;
    ULONG ReceivedMasterAbort  :1;
    ULONG RsvdZ  :1;
    ULONG UnexpectedSplitCompletionError  :1;
    ULONG UncorrectableSplitCompletion  :1;
    ULONG UncorrectableDataError  :1;
    ULONG UncorrectableAttributeError  :1;
    ULONG UncorrectableAddressError  :1;
    ULONG DelayedTransactionDiscardTimerExpired  :1;
    ULONG PERRAsserted  :1;
    ULONG SERRAsserted  :1;
    ULONG InternalBridgeError  :1;
    ULONG Reserved  :18;
  };
  ULONG  AsULONG;
} PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK, *PPCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK;
````


## -struct-fields
<dl>

### -field TargetAbortOnSplitCompletion

<dd>
<p>A single bit that indicates that the reporting of target aborts on split completion is masked.</p>
</dd>

### -field MasterAbortOnSplitCompletion

<dd>
<p>A single bit that indicates that the reporting of master aborts on split completion is masked.</p>
</dd>

### -field ReceivedTargetAbort

<dd>
<p>A single bit that indicates that the reporting of target aborts is masked.</p>
</dd>

### -field ReceivedMasterAbort

<dd>
<p>A single bit that indicates that the reporting of master aborts is masked.</p>
</dd>

### -field RsvdZ

<dd>
<p>Reserved for system use.</p>
</dd>

### -field UnexpectedSplitCompletionError

<dd>
<p>A single bit that indicates that the reporting of unexpected split completion errors is masked.</p>
</dd>

### -field UncorrectableSplitCompletion

<dd>
<p>A single bit that indicates that the reporting of uncorrectable split completion message data errors is masked.</p>
</dd>

### -field UncorrectableDataError

<dd>
<p>A single bit that indicates that the reporting of uncorrectable data errors is masked.</p>
</dd>

### -field UncorrectableAttributeError

<dd>
<p>A single bit that indicates that the reporting of uncorrectable attribute errors is masked.</p>
</dd>

### -field UncorrectableAddressError

<dd>
<p>A single bit that indicates that the reporting of uncorrectable address errors is masked.</p>
</dd>

### -field DelayedTransactionDiscardTimerExpired

<dd>
<p>A single bit that indicates that the reporting of the expiration of the delayed transaction discard timer is masked.</p>
</dd>

### -field PERRAsserted

<dd>
<p>A single bit that indicates that the reporting of PERR# assertions is masked.</p>
</dd>

### -field SERRAsserted

<dd>
<p>A single bit that indicates that the reporting of SERR# assertions is masked.</p>
</dd>

### -field InternalBridgeError

<dd>
<p>A single bit that indicates that the reporting of internal bridge errors is masked.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
</dd>

### -field AsULONG

<dd>
<p>A ULONG representation of the contents of the PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537458">PCI_EXPRESS_BRIDGE_AER_CAPABILITY</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h or Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537458">PCI_EXPRESS_BRIDGE_AER_CAPABILITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_SEC_UNCORRECTABLE_ERROR_MASK union%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
