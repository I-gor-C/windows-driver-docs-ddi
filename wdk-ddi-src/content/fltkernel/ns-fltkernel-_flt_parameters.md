---
UID: NS:fltkernel._FLT_PARAMETERS
title: "_FLT_PARAMETERS"
author: windows-driver-content
description: The FLT_PARAMETERS union defines the request-type-specific parameters associated with an I/O operation.
old-location: ifsk\flt_parameters.htm
old-project: ifsk
ms.assetid: 62aa20b7-ce5c-4d42-bce2-1d76a98887ed
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFLT_PARAMETERS, FLT_PARAMETERS, FLT_PARAMETERS union [Installable File System Drivers], FltSystemStructures_2ebb0ec7-76cc-49a3-b2ec-186f67369bbb.xml, PFLT_PARAMETERS, PFLT_PARAMETERS union pointer [Installable File System Drivers], _FLT_PARAMETERS, fltkernel/FLT_PARAMETERS, fltkernel/PFLT_PARAMETERS, ifsk.flt_parameters"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	fltkernel.h
api_name:
-	FLT_PARAMETERS
product: Windows
targetos: Windows
req.typenames: FLT_PARAMETERS, *PFLT_PARAMETERS
---

# _FLT_PARAMETERS structure
The FLT_PARAMETERS union defines the request-type-specific parameters associated with an I/O operation.

## Syntax
```
typedef struct _FLT_PARAMETERS {
  struct {
    LARGE_INTEGER            AllocationSize;
    PVOID                    EaBuffer;
    ULONG POINTER_ALIGNMENT  EaLength;
    USHORT POINTER_ALIGNMENT FileAttributes;
    ULONG                    Options;
    PIO_SECURITY_CONTEXT     SecurityContext;
    USHORT                   ShareAccess;
  } Create;
  struct {
    ULONG                    Options;
    PVOID                    Parameters;
    USHORT POINTER_ALIGNMENT Reserved;
    PIO_SECURITY_CONTEXT     SecurityContext;
    USHORT                   ShareAccess;
  } CreatePipe;
  struct {
    ULONG                    Options;
    PVOID                    Parameters;
    USHORT POINTER_ALIGNMENT Reserved;
    PIO_SECURITY_CONTEXT     SecurityContext;
    USHORT                   ShareAccess;
  } CreateMailslot;
  struct {
    LARGE_INTEGER           ByteOffset;
    ULONG POINTER_ALIGNMENT Key;
    ULONG                   Length;
    PMDL                    MdlAddress;
    PVOID                   ReadBuffer;
  } Read;
  struct {
    LARGE_INTEGER           ByteOffset;
    ULONG POINTER_ALIGNMENT Key;
    ULONG                   Length;
    PMDL                    MdlAddress;
    PVOID                   WriteBuffer;
  } Write;
  struct {
    FILE_INFORMATION_CLASS POINTER_ALIGNMENT FileInformationClass;
    PVOID                                    InfoBuffer;
    ULONG                                    Length;
  } QueryFileInformation;
  struct {
    FILE_INFORMATION_CLASS POINTER_ALIGNMENT FileInformationClass;
    PVOID                                    InfoBuffer;
    ULONG                                    Length;
    PFILE_OBJECT                             ParentOfTarget;
    struct {
      struct {
        BOOLEAN AdvanceOnly;
        BOOLEAN ReplaceIfExists;
      };
      ULONG  ClusterCount;
      HANDLE DeleteHandle;
    };
  } SetFileInformation;
  struct {
    PVOID                   EaBuffer;
    ULONG POINTER_ALIGNMENT EaIndex;
    PVOID                   EaList;
    ULONG                   EaListLength;
    ULONG                   Length;
    PMDL                    MdlAddress;
  } QueryEa;
  struct {
    PVOID EaBuffer;
    ULONG Length;
    PMDL  MdlAddress;
  } SetEa;
  struct {
    FS_INFORMATION_CLASS POINTER_ALIGNMENT FsInformationClass;
    ULONG                                  Length;
    PVOID                                  VolumeBuffer;
  } QueryVolumeInformation;
  struct {
    FS_INFORMATION_CLASS POINTER_ALIGNMENT FsInformationClass;
    ULONG                                  Length;
    PVOID                                  VolumeBuffer;
  } SetVolumeInformation;
  union {
    struct {
      ULONG                   Length;
      PUNICODE_STRING         FileName;
      FILE_INFORMATION_CLASS  FileInformationClass;
      ULONG POINTER_ALIGNMENT FileIndex;
      PVOID                   DirectoryBuffer;
      PMDL                    MdlAddress;
    } QueryDirectory;
    struct {
      ULONG                   Length;
      ULONG POINTER_ALIGNMENT CompletionFilter;
      ULONG POINTER_ALIGNMENT Spare1;
      ULONG POINTER_ALIGNMENT Spare2;
      PVOID                   DirectoryBuffer;
      PMDL                    MdlAddress;
    } NotifyDirectory;
    struct {
      ULONG                                                Length;
      ULONG POINTER_ALIGNMENT                              CompletionFilter;
      DIRECTORY_NOTIFY_INFORMATION_CLASS POINTER_ALIGNMENT DirectoryNotifyInformationClass;
      ULONG POINTER_ALIGNMENT                              Spare2;
      PVOID                                                DirectoryBuffer;
      PMDL                                                 MdlAddress;
    } NotifyDirectoryEx;
  } DirectoryControl;
  union {
    struct {
      PVPB           Vpb;
      PDEVICE_OBJECT DeviceObject;
    } VerifyVolume;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
    } Common;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
      PVOID                   InputBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Neither;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
      PVOID                   SystemBuffer;
    } Buffered;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
      PVOID                   InputSystemBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Direct;
  } FileSystemControl;
  union {
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
    } Common;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   InputBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Neither;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   SystemBuffer;
    } Buffered;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   InputSystemBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Direct;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   InputBuffer;
      PVOID                   OutputBuffer;
    } FastIo;
  } DeviceIoControl;
  struct {
    LARGE_INTEGER           ByteOffset;
    BOOLEAN                 ExclusiveLock;
    BOOLEAN                 FailImmediately;
    ULONG POINTER_ALIGNMENT Key;
    PLARGE_INTEGER          Length;
    PEPROCESS               ProcessId;
  } LockControl;
  struct {
    ULONG POINTER_ALIGNMENT Length;
    PMDL                    MdlAddress;
    PVOID                   SecurityBuffer;
    SECURITY_INFORMATION    SecurityInformation;
  } QuerySecurity;
  struct {
    PSECURITY_DESCRIPTOR SecurityDescriptor;
    SECURITY_INFORMATION SecurityInformation;
  } SetSecurity;
  struct {
    PVOID     Buffer;
    ULONG     BufferSize;
    PVOID     DataPath;
    ULONG_PTR ProviderId;
  } WMI;
  struct {
    ULONG                       Length;
    PMDL                        MdlAddress;
    PVOID                       QuotaBuffer;
    PFILE_GET_QUOTA_INFORMATION SidList;
    ULONG                       SidListLength;
    PSID                        StartSid;
  } QueryQuota;
  struct {
    ULONG Length;
    PMDL  MdlAddress;
    PVOID QuotaBuffer;
  } SetQuota;
  union {
    struct {
      PCM_RESOURCE_LIST AllocatedResources;
      PCM_RESOURCE_LIST AllocatedResourcesTranslated;
    } StartDevice;
    struct {
      DEVICE_RELATION_TYPE Type;
    } QueryDeviceRelations;
    struct {
      CONST GUID *InterfaceType;
      USHORT     Size;
      USHORT     Version;
      PINTERFACE Interface;
      PVOID      InterfaceSpecificData;
    } QueryInterface;
    struct {
      PDEVICE_CAPABILITIES Capabilities;
    } DeviceCapabilities;
    struct {
      PIO_RESOURCE_REQUIREMENTS_LIST IoResourceRequirementList;
    } FilterResourceRequirements;
    struct {
      ULONG                   WhichSpace;
      PVOID                   Buffer;
      ULONG                   Offset;
      ULONG POINTER_ALIGNMENT Length;
    } ReadWriteConfig;
    struct {
      BOOLEAN Lock;
    } SetLock;
    struct {
      BUS_QUERY_ID_TYPE IdType;
    } QueryId;
    struct {
      DEVICE_TEXT_TYPE       DeviceTextType;
      LCID POINTER_ALIGNMENT LocaleId;
    } QueryDeviceText;
    struct {
      BOOLEAN                                          InPath;
      BOOLEAN                                          Reserved[3];
      DEVICE_USAGE_NOTIFICATION_TYPE POINTER_ALIGNMENT Type;
    } UsageNotification;
  } Pnp;
  struct {
    PFS_FILTER_SECTION_SYNC_OUTPUT OutputInformation;
    ULONG                          PageProtection;
    FS_FILTER_SECTION_SYNC_TYPE    SyncType;
  } AcquireForSectionSynchronization;
  struct {
    PLARGE_INTEGER EndingOffset;
    PERESOURCE     *ResourceToRelease;
  } AcquireForModifiedPageWriter;
  struct {
    PERESOURCE ResourceToRelease;
  } ReleaseForModifiedPageWriter;
  struct {
    PVOID                  FileInformation;
    FILE_INFORMATION_CLASS FileInformationClass;
    PIRP                   Irp;
    PULONG                 Length;
  } QueryOpen;
  struct {
    BOOLEAN POINTER_ALIGNMENT CheckForReadOperation;
    LARGE_INTEGER             FileOffset;
    ULONG                     Length;
    ULONG POINTER_ALIGNMENT   LockKey;
  } FastIoCheckIfPossible;
  struct {
    PIRP                           Irp;
    PFILE_NETWORK_OPEN_INFORMATION NetworkInformation;
  } NetworkQueryOpen;
  struct {
    LARGE_INTEGER           FileOffset;
    ULONG POINTER_ALIGNMENT Key;
    ULONG POINTER_ALIGNMENT Length;
    PMDL                    *MdlChain;
  } MdlRead;
  struct {
    PMDL MdlChain;
  } MdlReadComplete;
  struct {
    LARGE_INTEGER           FileOffset;
    ULONG POINTER_ALIGNMENT Key;
    ULONG POINTER_ALIGNMENT Length;
    PMDL                    *MdlChain;
  } PrepareMdlWrite;
  struct {
    LARGE_INTEGER FileOffset;
    PMDL          MdlChain;
  } MdlWriteComplete;
  struct {
    ULONG DeviceType;
  } MountVolume;
  struct {
    PVOID         Argument1;
    PVOID         Argument2;
    PVOID         Argument3;
    PVOID         Argument4;
    PVOID         Argument5;
    LARGE_INTEGER Argument6;
  } Others;
} *PFLT_PARAMETERS, FLT_PARAMETERS;
```

## Members


## Remarks
This structure is stored in the <b>Parameters</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544638">FLT_IO_PARAMETER_BLOCK</a> structure for the operation. (A pointer to the FLT_IO_PARAMETER_BLOCK structure is stored in the <b>Iopb</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> structure for the operation.) 

For the specific FLT_PARAMETERS union component used in each type of I/O operation, see the following reference entries. 


<a href="https://msdn.microsoft.com/library/windows/hardware/ff544687">FLT_PARAMETERS for IRP_MJ_CREATE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544692">FLT_PARAMETERS for IRP_MJ_DEVICE_CONTROL and IRP_MJ_INTERNAL_DEVICE_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544695">FLT_PARAMETERS for IRP_MJ_DIRECTORY_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544705">FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544709">FLT_PARAMETERS for IRP_MJ_LOCK_CONTROL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544742">FLT_PARAMETERS for IRP_MJ_PNP</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544751">FLT_PARAMETERS for IRP_MJ_QUERY_EA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544756">FLT_PARAMETERS for IRP_MJ_QUERY_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544759">FLT_PARAMETERS for IRP_MJ_QUERY_QUOTA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544765">FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544768">FLT_PARAMETERS for IRP_MJ_QUERY_VOLUME_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544770">FLT_PARAMETERS for IRP_MJ_READ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544781">FLT_PARAMETERS for IRP_MJ_SET_EA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544789">FLT_PARAMETERS for IRP_MJ_SET_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544792">FLT_PARAMETERS for IRP_MJ_SET_QUOTA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544794">FLT_PARAMETERS for IRP_MJ_SET_SECURITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544798">FLT_PARAMETERS for IRP_MJ_SET_VOLUME_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544808">FLT_PARAMETERS for IRP_MJ_WRITE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544678">FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_MOD_WRITE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544684">FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544700">FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544713">FLT_PARAMETERS for IRP_MJ_MDL_READ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544719">FLT_PARAMETERS for IRP_MJ_MDL_READ_COMPLETE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544725">FLT_PARAMETERS for IRP_MJ_MDL_WRITE_COMPLETE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544731">FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544749">FLT_PARAMETERS for IRP_MJ_PREPARE_MDL_WRITE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544774">FLT_PARAMETERS for IRP_MJ_RELEASE_FOR_MOD_WRITE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544804">FLT_PARAMETERS for IRP_MJ_VOLUME_MOUNT</a>


The following I/O operations do not have parameters:

<ul>
<li>IRP_MJ_ACQUIRE_FOR_CC_FLUSH</li>
<li>IRP_MJ_CLEANUP</li>
<li>IRP_MJ_CLOSE</li>
<li>IRP_MJ_FLUSH_BUFFERS</li>
<li>IRP_MJ_RELEASE_FOR_CC_FLUSH</li>
<li>IRP_MJ_RELEASE_FOR_SECTION_SYNCHRONIZATION</li>
<li>IRP_MJ_SHUTDOWN</li>
<li>IRP_MJ_VOLUME_DISMOUNT</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | fltkernel.h (include Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544638">FLT_IO_PARAMETER_BLOCK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>