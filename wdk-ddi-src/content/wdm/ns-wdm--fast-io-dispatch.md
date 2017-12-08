---
UID: NS.wdm._FAST_IO_DISPATCH
title: FAST_IO_DISPATCH
author: windows-driver-content
description: Contains a set of callback routines that a file system driver or file system filter driver (legacy) provides for fast I/O processing.
old-location: ifsk\fast_io_dispatch.htm
old-project: ifsk
ms.assetid: 9F422CE9-8ADC-4709-8FE5-5A3501B47AC2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FAST_IO_DISPATCH, FAST_IO_DISPATCH, *PFAST_IO_DISPATCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FAST_IO_DISPATCH
req.alt-loc: Wdm.h
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

# FAST_IO_DISPATCH structure



## -description
<p>Contains a set of callback routines that a file system driver or file system filter driver (legacy) provides for fast I/O processing.</p>


## -syntax

````
typedef struct _FAST_IO_DISPATCH {
  ULONG                                  SizeOfFastIoDispatch;
  PFAST_IO_CHECK_IF_POSSIBLE             FastIoCheckIfPossible;
  PFAST_IO_READ                          FastIoRead;
  PFAST_IO_WRITE                         FastIoWrite;
  PFAST_IO_QUERY_BASIC_INFO              FastIoQueryBasicInfo;
  PFAST_IO_QUERY_STANDARD_INFO           FastIoQueryStandardInfo;
  PFAST_IO_LOCK                          FastIoLock;
  PFAST_IO_UNLOCK_SINGLE                 FastIoUnlockSingle;
  PFAST_IO_UNLOCK_ALL                    FastIoUnlockAll;
  PFAST_IO_UNLOCK_ALL_BY_KEY             FastIoUnlockAllByKey;
  PFAST_IO_DEVICE_CONTROL                FastIoDeviceControl;
  PFAST_IO_ACQUIRE_FILE                  AcquireFileForNtCreateSection;
  PFAST_IO_RELEASE_FILE                  ReleaseFileForNtCreateSection;
  PFAST_IO_DETACH_DEVICE                 FastIoDetachDevice;
  PFAST_IO_QUERY_NETWORK_OPEN_INFO       FastIoQueryNetworkOpenInfo;
  PFAST_IO_ACQUIRE_FOR_MOD_WRITE         AcquireForModWrite;
  PFAST_IO_MDL_READ                      MdlRead;
  PFAST_IO_MDL_READ_COMPLETE             MdlReadComplete;
  PFAST_IO_PREPARE_MDL_WRITE             PrepareMdlWrite;
  PFAST_IO_MDL_WRITE_COMPLETE            MdlWriteComplete;
  PFAST_IO_READ_COMPRESSED               FastIoReadCompressed;
  PFAST_IO_WRITE_COMPRESSED              FastIoWriteCompressed;
  PFAST_IO_MDL_READ_COMPLETE_COMPRESSED  MdlReadCompleteCompressed;
  PFAST_IO_MDL_WRITE_COMPLETE_COMPRESSED MdlWriteCompleteCompressed;
  PFAST_IO_QUERY_OPEN                    FastIoQueryOpen;
  PFAST_IO_RELEASE_FOR_MOD_WRITE         ReleaseForModWrite;
  PFAST_IO_ACQUIRE_FOR_CCFLUSH           AcquireForCcFlush;
  PFAST_IO_RELEASE_FOR_CCFLUSH           ReleaseForCcFlush;
} FAST_IO_DISPATCH, *PFAST_IO_DISPATCH;
````


## -struct-fields
<dl>

### -field SizeOfFastIoDispatch

<dd>
<p>Set to <b>sizeof</b>(FAST_IO_DISPATCH).</p>
</dd>

### -field FastIoCheckIfPossible

<dd>
<p>A pointer to a callback routine that checks if fast I/O is possible for a either a read or a write operation.</p>
</dd>

### -field FastIoRead

<dd>
<p>A pointer to a callback routine that does a fast cached read, bypassing the IRP read path.  It is used to perform a copy read
    for a cached file object.</p>
</dd>

### -field FastIoWrite

<dd>
<p>A pointer to a callback routine that does a fast cached write, bypassing the IRP write path.  It is used to perform a copy write
    for a cached file object.</p>
</dd>

### -field FastIoQueryBasicInfo

<dd>
<p>A pointer to a callback routine for fast query of basic file information.</p>
</dd>

### -field FastIoQueryStandardInfo

<dd>
<p>A pointer to a callback routine for fast query of standard file information.</p>
</dd>

### -field FastIoLock

<dd>
<p>A pointer to a callback routine for doing a fast lock on a file object.</p>
</dd>

### -field FastIoUnlockSingle

<dd>
<p>A pointer to a callback routine for doing a fast release of a single lock on a file object.</p>
</dd>

### -field FastIoUnlockAll

<dd>
<p>A pointer to a callback routine for doing a fast release of a all locks held on a file object.</p>
</dd>

### -field FastIoUnlockAllByKey

<dd>
<p>A pointer to a callback routine for doing a fast release of a all locks grouped by a key.</p>
</dd>

### -field FastIoDeviceControl

<dd>
<p>A pointer to a callback routine for fast device control processing.</p>
</dd>

### -field AcquireFileForNtCreateSection

<dd>
<p>A pointer to a callback routine used by the memory manager to acquire a file exclusively.</p>
</dd>

### -field ReleaseFileForNtCreateSection

<dd>
<p>A pointer to a callback routine used by the memory manager to release a previously acquired file.</p>
</dd>

### -field FastIoDetachDevice

<dd>
<p>A pointer to a callback routine that is invoked to detach the current device object from a device object that
    is being deleted. </p>
</dd>

### -field FastIoQueryNetworkOpenInfo

<dd>
<p>A pointer to a callback routine for fast query of network file information.</p>
</dd>

### -field AcquireForModWrite

<dd>
<p>A pointer to a callback routine that decides which file system resource the modified page
    writer should acquire and acquires it if possible.</p>
</dd>

### -field MdlRead

<dd>
<p>A pointer to a callback routine that does a fast cached MDL read, bypassing the IRP read path.  It is used to perform a copy read
    for a cached file object.</p>
</dd>

### -field MdlReadComplete

<dd>
<p>A pointer to a callback routine that performs a fast completion of an MDL read.</p>
</dd>

### -field PrepareMdlWrite

<dd>
<p>A pointer to a callback routine that does a fast cached MDL write, bypassing the IRP write path.  It is used to perform a copy write
    for a cached file object.</p>
</dd>

### -field MdlWriteComplete

<dd>
<p>A pointer to a callback routine that performs a fast completion of an MDL write.</p>
</dd>

### -field FastIoReadCompressed

<dd>
<p>A pointer to a callback routine that performs a fast  compressed read of data from a file.</p>
</dd>

### -field FastIoWriteCompressed

<dd>
<p>A pointer to a callback routine that performs a fast  compressed write of data to  a file.</p>
</dd>

### -field MdlReadCompleteCompressed

<dd>
<p>A pointer to a callback routine that completes  a fast  MDL compressed read of data from  a file.</p>
</dd>

### -field MdlWriteCompleteCompressed

<dd>
<p>A pointer to a callback routine that completes  a fast  MDL compressed write of data to  a file.</p>
</dd>

### -field FastIoQueryOpen

<dd>
<p>A pointer to a callback routine that implements  a fast  open for path based queries.</p>
</dd>

### -field ReleaseForModWrite

<dd>
<p>This routine releases a file system resource previously acquired for
    the modified page write.</p>
</dd>

### -field AcquireForCcFlush

<dd>
<p>A pointer to a callback routine that acquires a file system resource prior to a cache flush.</p>
</dd>

### -field ReleaseForCcFlush

<dd>
<p>A pointer to a callback routine that releases a file system resource previously acquired for a cache flush.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>