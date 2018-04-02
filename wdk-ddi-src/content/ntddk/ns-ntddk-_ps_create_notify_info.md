---
UID: NS:ntddk._PS_CREATE_NOTIFY_INFO
title: "_PS_CREATE_NOTIFY_INFO"
author: windows-driver-content
description: The PS_CREATE_NOTIFY_INFO structure provides information about a newly created process.
old-location: kernel\ps_create_notify_info.htm
old-project: kernel
ms.assetid: 66fade6b-b1c1-477c-bd44-2809d02271f2
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPS_CREATE_NOTIFY_INFO, PPS_CREATE_NOTIFY_INFO, PPS_CREATE_NOTIFY_INFO structure pointer [Kernel-Mode Driver Architecture], PS_CREATE_NOTIFY_INFO, PS_CREATE_NOTIFY_INFO structure [Kernel-Mode Driver Architecture], _PS_CREATE_NOTIFY_INFO, kernel.ps_create_notify_info, kstruct_c_489ee208-518d-41f1-af90-a8873f3e7fb0.xml, ntddk/PPS_CREATE_NOTIFY_INFO, ntddk/PS_CREATE_NOTIFY_INFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
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
-	Ntddk.h
api_name:
-	PS_CREATE_NOTIFY_INFO
product: Windows
targetos: Windows
req.typenames: PS_CREATE_NOTIFY_INFO, *PPS_CREATE_NOTIFY_INFO
---

# _PS_CREATE_NOTIFY_INFO structure
The <b>PS_CREATE_NOTIFY_INFO</b> structure provides information about a newly created process.

## Syntax
```
typedef struct _PS_CREATE_NOTIFY_INFO {
  SIZE_T           Size;
  union {
    ULONG Flags;
    struct {
      ULONG  : 1  FileOpenNameAvailable;
      ULONG  : 1  IsSubsystemProcess;
      ULONG  : 30 Reserved;
    };
  };
  HANDLE           ParentProcessId;
  CLIENT_ID        CreatingThreadId;
  _FILE_OBJECT     *FileObject;
  struct           _FILE_OBJECT;
  PCUNICODE_STRING ImageFileName;
  PCUNICODE_STRING CommandLine;
  NTSTATUS         CreationStatus;
} PS_CREATE_NOTIFY_INFO, *PPS_CREATE_NOTIFY_INFO;
```

## Members


`Size`

The size, in bytes, of this structure. The operating system uses this size to indicate the type of structure that it passes to <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951">CreateProcessNotifyEx</a>. Currently, this member is always <b>sizeof</b>(<b>PS_CREATE_NOTIFY_INFO</b>).

`ParentProcessId`

The process ID of the parent process for the new process. Note that the parent process is not necessarily the same process as the process that created the new process. The new process can inherit certain properties of the parent process, such as handles or shared memory. (The process ID of the process creator is given by <b>CreatingThreadId</b>-&gt;<b>UniqueProcess</b>.)

`CreatingThreadId`

The process ID and thread ID of the process and thread that created the new process. <b>CreatingThreadId</b>-&gt;<b>UniqueProcess</b> contains the process ID, and <b>CreatingThreadId</b>-&gt;<b>UniqueThread</b> contains the thread ID.

`FileObject`

A pointer to the file object for the process executable file. 

<div class="alert"><b>Note</b>  <p class="note">If <b>IsSubsystemProcess</b> is TRUE, this value may be NULL. 

</div>
<div> </div>

`ImageFileName`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> string that holds the file name of the executable. If the <b>FileOpenNameAvailable</b> member is <b>TRUE</b>, the string specifies the exact file name that is used to open the executable file. If <b>FileOpenNameAvailable</b> is <b>FALSE</b>, the operating system might provide only a partial name.

<div class="alert"><b>Note</b>  <p class="note">If <b>IsSubsystemProcess</b> is TRUE, this value maybe NULL. 

</div>
<div> </div>

`CommandLine`

A pointer to a <b>UNICODE_STRING</b> string that holds the command that is used to execute the process. If the command is not available, <b>CommandLine</b> is <b>NULL</b>.

<div class="alert"><b>Note</b>  <p class="note">If <b>IsSubsystemProcess</b> is TRUE, this value maybe NULL. 

</div>
<div> </div>

`CreationStatus`

The NTSTATUS value to return for the process-creation operation. Drivers can change this value to an error code to prevent the process from being created.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating system. Available in Windows Vista and later versions of the Windows operating system. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff559951">CreateProcessNotifyEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559953">PsSetCreateProcessNotifyRoutineEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>