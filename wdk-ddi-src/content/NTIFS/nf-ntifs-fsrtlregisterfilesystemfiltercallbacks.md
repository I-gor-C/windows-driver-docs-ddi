---
UID: NF.ntifs.FsRtlRegisterFileSystemFilterCallbacks
title: FsRtlRegisterFileSystemFilterCallbacks
author: windows-driver-content
description: File system filter drivers and file systems call the FsRtlRegisterFileSystemFilterCallbacks routine to register notification callback routines to be invoked when the underlying file system performs certain operations.
old-location: ifsk\fsrtlregisterfilesystemfiltercallbacks.htm
ms.assetid: cd6d2ab6-ce17-47db-b5d0-4f9543e15487
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlRegisterFileSystemFilterCallbacks
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: FsRtlRegisterFileSystemFilterCallbacks
req.iface: 
---

# FsRtlRegisterFileSystemFilterCallbacks function



## -description
<p>File system filter drivers and file systems call the <b>FsRtlRegisterFileSystemFilterCallbacks</b> routine to register notification callback routines to be invoked when the underlying file system performs certain operations. </p>


## -syntax

````
NTSTATUS FsRtlRegisterFileSystemFilterCallbacks(
  _In_ struct _DRIVER_OBJECT *FilterDriverObject,
  _In_ PFS_FILTER_CALLBACKS  Callbacks
);
````


## -parameters
<dl>

### -param <i>FilterDriverObject</i> [in]

<dd>
<p>A pointer to the driver object for the filter or file system driver. </p>
</dd>

### -param <i>Callbacks</i> [in]

<dd>
<p>A pointer to a structure that contains the entry points of caller-supplied notification callback routines. </p>
<p>This structure is defined as follows. </p>
<div class="alert"><b>Note</b>  All of the callback entry points are optional and can be <b>NULL</b>. </div>
<div> </div>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _FS_FILTER_CALLBACKS {
    ULONG SizeOfFsFilterCallbacks;
    ULONG Reserved;
    PFS_FILTER_CALLBACK PreAcquireForSectionSynchronization;
    PFS_FILTER_COMPLETION_CALLBACK PostAcquireForSectionSynchronization;
    PFS_FILTER_CALLBACK PreReleaseForSectionSynchronization;
    PFS_FILTER_COMPLETION_CALLBACK PostReleaseForSectionSynchronization;
    PFS_FILTER_CALLBACK PreAcquireForCcFlush;
    PFS_FILTER_COMPLETION_CALLBACK PostAcquireForCcFlush;
    PFS_FILTER_CALLBACK PreReleaseForCcFlush;
    PFS_FILTER_COMPLETION_CALLBACK PostReleaseForCcFlush;
    PFS_FILTER_CALLBACK PreAcquireForModifiedPageWriter;
    PFS_FILTER_COMPLETION_CALLBACK PostAcquireForModifiedPageWriter;
    PFS_FILTER_CALLBACK PreReleaseForModifiedPageWriter;
    PFS_FILTER_COMPLETION_CALLBACK PostReleaseForModifiedPageWriter;
} FS_FILTER_CALLBACKS, *PFS_FILTER_CALLBACKS;</pre>
</td>
</tr>
</table></span></div>
<p>The filter callback routine and its parameters are defined as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
NTSTATUS (*PFS_FILTER_CALLBACK) (
              IN PFS_FILTER_CALLBACK_DATA Data,
              OUT PVOID *CompletionContext
              );</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Parameter</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><i>Data</i></p>
</td>
<td>
<p>Pointer to the callback data structure for this operation.</p>
</td>
</tr>
<tr>
<td>
<p><i>CompletionContext</i></p>
</td>
<td>
<p>Context information to be passed to the filter completion callback routine. Set to <b>NULL</b> if no context information is to be passed or if there is no corresponding filter completion callback routine.</p>
</td>
</tr>
</table>
<p> </p>
<p>The filter completion callback routine and its parameters are defined as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
VOID (*PFS_FILTER_COMPLETION_CALLBACK) (
          IN PFS_FILTER_CALLBACK_DATA Data,
          IN NTSTATUS OperationStatus,
          IN PVOID CompletionContext
          );</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Parameter</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><i>Data</i></p>
</td>
<td>
<p>Pointer to the callback data structure for this operation.</p>
</td>
</tr>
<tr>
<td>
<p><i>OperationStatus</i></p>
</td>
<td>
<p>Status of the operation. If the file system successfully performed the operation, this parameter is set to STATUS_SUCCESS. Otherwise, it is set to an appropriate error status value.</p>
</td>
</tr>
<tr>
<td>
<p><i>CompletionContext</i></p>
</td>
<td>
<p>Context information that was set in the filter callback routine. This is set to <b>NULL</b> if no information is passed or if there is no corresponding filter callback routine.</p>
</td>
</tr>
</table>
<p> </p>
<p>The callback data structure and its members are defined as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _FS_FILTER_CALLBACK_DATA {
    ULONG SizeOfFsFilterCallbackData;
    UCHAR Operation;
    UCHAR Reserved;
    struct _DEVICE_OBJECT *DeviceObject;
    struct _FILE_OBJECT *FileObject;
    FS_FILTER_PARAMETERS Parameters;
} FS_FILTER_CALLBACK_DATA, *PFS_FILTER_CALLBACK_DATA;</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Member</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>SizeOfFsFilterCallbackData</b></p>
</td>
<td>
<p>Size of the callback data structure.</p>
</td>
</tr>
<tr>
<td>
<p><b>Operation</b></p>
</td>
<td>
<p>File system operation for which the callback routine is to be invoked. This operation can be one of the following: 
	<ul>
<li>FS_FILTER_ACQUIRE_FOR_SECTION_SYNCHRONIZATION</li>
<li>FS_FILTER_RELEASE_FOR_SECTION_SYNCHRONIZATION</li>
<li>FS_FILTER_ACQUIRE_FOR_MOD_WRITE</li>
<li>FS_FILTER_RELEASE_FOR_MOD_WRITE</li>
<li>FS_FILTER_ACQUIRE_FOR_CC_FLUSH</li>
<li>FS_FILTER_RELEASE_FOR_CC_FLUSH</li>
</ul>
</p>
</td>
</tr>
<tr>
<td>
<p><b>Reserved</b></p>
</td>
<td>
<p>Reserved for system use.</p>
</td>
</tr>
<tr>
<td>
<p><b>DeviceObject</b></p>
</td>
<td>
<p>Device object for this operation.</p>
</td>
</tr>
<tr>
<td>
<p><b>FileObject</b></p>
</td>
<td>
<p>File object for this operation.</p>
</td>
</tr>
<tr>
<td>
<p><b>Parameters</b></p>
</td>
<td>
<p>Union containing any operation-specific parameters.</p>
</td>
</tr>
</table>
<p> </p>
<p>The filter parameter union is defined as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _FS_FILTER_PARAMETERS {
    struct {
        PLARGE_INTEGER EndingOffset;
        PERESOURCE *ResourceToRelease;
    } AcquireForModifiedPageWriter;
    struct {
        PERESOURCE ResourceToRelease;
    } ReleaseForModifiedPageWriter;
    struct {
 FS_FILTER_SECTION_SYNC_TYPE SyncType;
 ULONG PageProtection;
    } AcquireForSectionSynchronization;
    struct {
        PVOID Argument1;
        PVOID Argument2;
        PVOID Argument3;
        PVOID Argument4;
        PVOID Argument5;
    } Others;
} FS_FILTER_PARAMETERS, *PFS_FILTER_PARAMETERS;</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Parameter</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><i>EndingOffset</i></p>
</td>
<td>
<p>Offset of the last byte being written plus one.</p>
</td>
</tr>
<tr>
<td>
<p><i>ResourceToRelease</i></p>
</td>
<td>
<p>Resource to be released. This parameter must not have a <b>NULL</b> value.</p>
</td>
</tr>
<tr>
<td>
<p><i>SyncType</i></p>
</td>
<td>
<p>Type of synchronization requested for the section: SyncTypeCreateSection if a section is being created, SyncTypeOther otherwise.</p>
</td>
</tr>
<tr>
<td>
<p><i>PageProtection</i></p>
</td>
<td>
<p>Type of page protection requested for the section. Must be zero if <i>SyncType</i> is SyncTypeOther. Otherwise, one of the following flags, possibly ORed with PAGE_NOCACHE: <ul>
<li>PAGE_READONLY</li>
<li>PAGE_READWRITE</li>
<li>PAGE_WRITECOPY</li>
<li>PAGE_EXECUTE</li>
</ul>
</p>
</td>
</tr>
<tr>
<td>
<p><i>Argument1</i></p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td>
<p><i>Argument2</i></p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td>
<p><i>Argument3</i></p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td>
<p><i>Argument4</i></p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
<tr>
<td>
<p><i>Argument5</i></p>
</td>
<td>
<p>Reserved for future use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The <b>FsRtlRegisterFileSystemFilterCallbacks</b> routine can return one of the following status values: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callback routines were successfully registered. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FsRtlRegisterFileSystemFilterCallbacks</b> encountered a pool allocation failure when allocating memory to store the callback information. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters is invalid. </p>

<p> </p>

## -remarks
<p>File system and file system filter drivers should call <b>FsRtlRegisterFileSystemFilterCallbacks</b> from the driver's <b>DriverEntry</b> routine.  </p>

<p>File systems call <b>FsRtlRegisterFileSystemFilterCallbacks</b> to set the <b>PreAcquireForSectionSynchronization</b> callback member of the FS_FILTER_CALLBACKS structure instead of using the obsolete <b>AcquireFileForNtCreateSection</b>.</p>

<p><b>FsRtlRegisterFileSystemFilterCallbacks</b> registers the notification callback routines that were specified in the <i>Callbacks</i> parameter to be invoked when requests for certain file operations are sent to the underlying file system. </p>

<p>Callback routines are currently defined for the following operations: </p>

<p>The memory manager acquires a file exclusively before creating a memory-mapped section for a portion of the file. </p>

<p>
<div class="alert"><b>Note</b>  For this operation, <i>SyncType</i> is set to SyncTypeCreateSection.</div>
<div> </div>
</p>

<p>
<dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl><p>The memory manager releases a file after creating a memory-mapped section for a portion of the file. </p>

<p>
<dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl><p>A kernel component (such as the cache manager) acquires a file exclusively before temporarily disabling section creation for a portion of the file. </p>

<p>
<div class="alert"><b>Note</b>  For this operation, <i>SyncType</i> is set to SyncTypeOther.</div>
<div> </div>
</p>

<p>
<dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl><p>
<div class="alert"><b>Note</b>  PreAcquireForSectionSynchronization should always return a success status code (such as STATUS_SUCCESS) for this operation. Returning any other type of status code causes the system to ASSERT on a checked build. (On free builds, the status code is ignored.)</div>
<div> </div>
</p>

<p>A kernel component (such as the cache manager) releases a file after temporarily disabling section creation for a portion of the file. </p>

<p>
<dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl><p>The cache manager acquires a file exclusively before flushing a portion of the file from the cache. </p>

<p>
<dl>
<dt>PreAcquireForCcFlush</dt>
<dt>PostAcquireForCcFlush</dt>
</dl>
</p><dl>
<dt>PreAcquireForCcFlush</dt>
<dt>PostAcquireForCcFlush</dt>
</dl><p>The cache manager releases a file after flushing a portion of the file from the cache. </p>

<p>
<dl>
<dt>PreReleaseForCcFlush</dt>
<dt>PostReleaseForCcFlush</dt>
</dl>
</p><dl>
<dt>PreReleaseForCcFlush</dt>
<dt>PostReleaseForCcFlush</dt>
</dl><p>The modified page writer acquires a file exclusively before writing a portion of the file to disk. </p>

<p>
<dl>
<dt>PreAcquireForModifiedPageWriter</dt>
<dt>PostAcquireForModifiedPageWriter</dt>
</dl>
</p><dl>
<dt>PreAcquireForModifiedPageWriter</dt>
<dt>PostAcquireForModifiedPageWriter</dt>
</dl><p>The modified page writer releases a file after writing a portion of the file to disk. </p>

<p>
<dl>
<dt>PreReleaseForModifiedPageWriter</dt>
<dt>PostReleaseForModifiedPageWriter</dt>
</dl>
</p><dl>
<dt>PreReleaseForModifiedPageWriter</dt>
<dt>PostReleaseForModifiedPageWriter</dt>
</dl><p> </p>

<p>The filter notification callback routine is invoked before the operation request is passed to lower-level filter drivers and the underlying file system. In the callback routine, the filter driver should perform any needed processing and immediately return STATUS_SUCCESS. If a filter driver's callback routine returns a status value other than STATUS_SUCCESS, this causes the operation request to fail. Repeated failure of certain requests, such as locking requests, can halt system progress. Thus, filter drivers should fail such a request only when absolutely necessary. When failing these requests, the filter driver should return an error status value that describes the error as completely and accurately as possible. </p>

<p>PreReleaseForSectionSynchronization </p>

<p>PreReleaseForCcFlush </p>

<p>PreReleaseForModifiedPageWriter </p>

<p>The filter completion callback routine is invoked after the operation request is passed to lower-level filter drivers and the underlying file system. In the completion callback routine, the filter driver must perform any needed processing and immediately return. </p>

<p>The callback routines defined by <b>FsRtlRegisterFileSystemFilterCallbacks</b> supersede the following fast I/O callback routines, which are obsolete and should not be used by file system filter drivers: </p>

<p>AcquireForCcFlush</p>

<p>AcquireFileForNtCreateSection</p>

<p>AcquireForModWrite</p>

<p>ReleaseForCcFlush</p>

<p>ReleaseFileForNtCreateSection</p>

<p>ReleaseForModWrite</p>

<p>File system and file system filter drivers should call <b>FsRtlRegisterFileSystemFilterCallbacks</b> from the driver's <b>DriverEntry</b> routine.  </p>

<p>File systems call <b>FsRtlRegisterFileSystemFilterCallbacks</b> to set the <b>PreAcquireForSectionSynchronization</b> callback member of the FS_FILTER_CALLBACKS structure instead of using the obsolete <b>AcquireFileForNtCreateSection</b>.</p>

<p><b>FsRtlRegisterFileSystemFilterCallbacks</b> registers the notification callback routines that were specified in the <i>Callbacks</i> parameter to be invoked when requests for certain file operations are sent to the underlying file system. </p>

<p>Callback routines are currently defined for the following operations: </p>

<p>The memory manager acquires a file exclusively before creating a memory-mapped section for a portion of the file. </p>

<p>
<div class="alert"><b>Note</b>  For this operation, <i>SyncType</i> is set to SyncTypeCreateSection.</div>
<div> </div>
</p>

<p>
<dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl><p>The memory manager releases a file after creating a memory-mapped section for a portion of the file. </p>

<p>
<dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl><p>A kernel component (such as the cache manager) acquires a file exclusively before temporarily disabling section creation for a portion of the file. </p>

<p>
<div class="alert"><b>Note</b>  For this operation, <i>SyncType</i> is set to SyncTypeOther.</div>
<div> </div>
</p>

<p>
<dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreAcquireForSectionSynchronization</dt>
<dt>PostAcquireForSectionSynchronization</dt>
</dl><p>
<div class="alert"><b>Note</b>  PreAcquireForSectionSynchronization should always return a success status code (such as STATUS_SUCCESS) for this operation. Returning any other type of status code causes the system to ASSERT on a checked build. (On free builds, the status code is ignored.)</div>
<div> </div>
</p>

<p>A kernel component (such as the cache manager) releases a file after temporarily disabling section creation for a portion of the file. </p>

<p>
<dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl>
</p><dl>
<dt>PreReleaseForSectionSynchronization</dt>
<dt>PostReleaseForSectionSynchronization</dt>
</dl><p>The cache manager acquires a file exclusively before flushing a portion of the file from the cache. </p>

<p>
<dl>
<dt>PreAcquireForCcFlush</dt>
<dt>PostAcquireForCcFlush</dt>
</dl>
</p><dl>
<dt>PreAcquireForCcFlush</dt>
<dt>PostAcquireForCcFlush</dt>
</dl><p>The cache manager releases a file after flushing a portion of the file from the cache. </p>

<p>
<dl>
<dt>PreReleaseForCcFlush</dt>
<dt>PostReleaseForCcFlush</dt>
</dl>
</p><dl>
<dt>PreReleaseForCcFlush</dt>
<dt>PostReleaseForCcFlush</dt>
</dl><p>The modified page writer acquires a file exclusively before writing a portion of the file to disk. </p>

<p>
<dl>
<dt>PreAcquireForModifiedPageWriter</dt>
<dt>PostAcquireForModifiedPageWriter</dt>
</dl>
</p><dl>
<dt>PreAcquireForModifiedPageWriter</dt>
<dt>PostAcquireForModifiedPageWriter</dt>
</dl><p>The modified page writer releases a file after writing a portion of the file to disk. </p>

<p>
<dl>
<dt>PreReleaseForModifiedPageWriter</dt>
<dt>PostReleaseForModifiedPageWriter</dt>
</dl>
</p><dl>
<dt>PreReleaseForModifiedPageWriter</dt>
<dt>PostReleaseForModifiedPageWriter</dt>
</dl><p> </p>

<p>The filter notification callback routine is invoked before the operation request is passed to lower-level filter drivers and the underlying file system. In the callback routine, the filter driver should perform any needed processing and immediately return STATUS_SUCCESS. If a filter driver's callback routine returns a status value other than STATUS_SUCCESS, this causes the operation request to fail. Repeated failure of certain requests, such as locking requests, can halt system progress. Thus, filter drivers should fail such a request only when absolutely necessary. When failing these requests, the filter driver should return an error status value that describes the error as completely and accurately as possible. </p>

<p>PreReleaseForSectionSynchronization </p>

<p>PreReleaseForCcFlush </p>

<p>PreReleaseForModifiedPageWriter </p>

<p>The filter completion callback routine is invoked after the operation request is passed to lower-level filter drivers and the underlying file system. In the completion callback routine, the filter driver must perform any needed processing and immediately return. </p>

<p>The callback routines defined by <b>FsRtlRegisterFileSystemFilterCallbacks</b> supersede the following fast I/O callback routines, which are obsolete and should not be used by file system filter drivers: </p>

<p>AcquireForCcFlush</p>

<p>AcquireFileForNtCreateSection</p>

<p>AcquireForModWrite</p>

<p>ReleaseForCcFlush</p>

<p>ReleaseFileForNtCreateSection</p>

<p>ReleaseForModWrite</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Microsoft Windows XP and later versions of the Windows operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>