---
UID: NS.wdm._DEVICE_OBJECT
title: DEVICE_OBJECT
author: windows-driver-content
description: A device object represents a logical, virtual, or physical device for which a driver handles I/O requests.
old-location: kernel\device_object.htm
old-project: kernel
ms.assetid: f3522315-cf15-41f7-ac87-c625c7dc8040
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: DEVICE_OBJECT,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_OBJECT
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

# DEVICE_OBJECT structure



## -description
<p>The <b>DEVICE_OBJECT</b> structure is used by the operating system to represent a device object. A device object represents a logical, virtual, or physical device for which a driver handles I/O requests.</p>


## -syntax

````
typedef struct _DEVICE_OBJECT {
  CSHORT                      Type;
  USHORT                      Size;
  LONG                        ReferenceCount;
  struct _DRIVER_OBJECT  *DriverObject;
  struct _DEVICE_OBJECT  *NextDevice;
  struct _DEVICE_OBJECT  *AttachedDevice;
  struct _IRP  *CurrentIrp;
  PIO_TIMER                   Timer;
  ULONG                       Flags;
  ULONG                       Characteristics;
  __volatile PVPB             Vpb;
  PVOID                       DeviceExtension;
  DEVICE_TYPE                 DeviceType;
  CCHAR                       StackSize;
  union {
    LIST_ENTRY         ListEntry;
    WAIT_CONTEXT_BLOCK Wcb;
  } Queue;
  ULONG                       AlignmentRequirement;
  KDEVICE_QUEUE               DeviceQueue;
  KDPC                        Dpc;
  ULONG                       ActiveThreadCount;
  PSECURITY_DESCRIPTOR        SecurityDescriptor;
  KEVENT                      DeviceLock;
  USHORT                      SectorSize;
  USHORT                      Spare1;
  struct _DEVOBJ_EXTENSION  *  DeviceObjectExtension;
  PVOID                       Reserved;
} DEVICE_OBJECT, *PDEVICE_OBJECT;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Used by the operating system to indicate that an object is a device object. For device objects, the value of this member is 3. This is a read-only member.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of the device object. This size includes the driver-specified device extension pointed to by the <b>DeviceExtension</b> member, but does not include the opaque device object extension pointed to by the <b>DeviceObjectExtension</b> member. <b>Size</b> is a read-only member.</p>
</dd>

### -field <b>ReferenceCount</b>

<dd>
<p>Used by the I/O manager to track the number of open handles for the device that are associated with the device object. This allows the I/O manager to avoid unloading a driver when there are outstanding handles for the driver's device(s). This is a read-only member.</p>
</dd>

### -field <b>DriverObject</b>

<dd>
<p>A pointer to the driver object (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>), that represents the loaded image of the driver that was input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routines. This member is set by the I/O manager upon a successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407">IoCreateDeviceSecure</a>. This is a read-only member.</p>
</dd>

### -field <b>NextDevice</b>

<dd>
<p>A pointer to the next device object, if any, that was created by the same driver. The I/O manager updates this list at each successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407">IoCreateDeviceSecure</a>.</p>
<p>A non- Plug and Play (PnP) driver that is being unloaded must traverse ("walk") the list of its device objects and delete them. A PnP driver does not have to walk this list of device objects. Instead, PnP drivers perform their cleanup during the device removal PnP operation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a>).</p>
<p>A driver that recreates its device objects dynamically also uses this member. This is a read/write member.</p>
</dd>

### -field <b>AttachedDevice</b>

<dd>
<p>A pointer to the attached device object. If there is no attached device object, this member is <b>NULL</b>. The device object that is pointed to by the <b>AttachedDevice</b> member typically is the device object of a filter driver, which intercepts I/O requests originally targeted to the device represent by the device object. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548294">IoAttachDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548298">IoAttachDeviceByPointer</a> topics. This is an opaque member.</p>
</dd>

### -field <b>CurrentIrp</b>

<dd>
<p>A pointer to the current IRP if the driver has a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563858">StartIo</a> routine whose entry point was set in the driver object and if the driver is currently processing IRP(s). Otherwise, this member is <b>NULL</b>. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550370">IoStartPacket</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550358">IoStartNextPacket</a> topics. This is a read-only member.</p>
</dd>

### -field <b>Timer</b>

<dd>
<p>A pointer to a timer object. This allows the I/O manager to call a driver-supplied timer routine every second. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549344">IoInitializeTimer</a>. This is a read/write member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Device drivers perform a bitwise <b>OR</b> operation with this member in their newly created device objects by using one or more of the following system-defined values:</p>
<p></p>
<dl>

### -field <a id="DO_BUFFERED_IO_or_DO_DIRECT_IO"></a><a id="do_buffered_io_or_do_direct_io"></a><a id="DO_BUFFERED_IO_OR_DO_DIRECT_IO"></a>DO_BUFFERED_IO or DO_DIRECT_IO

<dd>
<p>Specifies the type of buffering that is used by the I/O manager for I/O requests that are sent to the device stack. Higher-level drivers OR this member with the same value as the next-lower driver in the stack, except possibly for highest-level drivers.</p>
</dd>

### -field <a id="DO_BUS_ENUMERATED_DEVICE"></a><a id="do_bus_enumerated_device"></a>DO_BUS_ENUMERATED_DEVICE

<dd>
<p>The operating system sets this flag in each physical device object (PDO). Drivers must not modify this flag.</p>
</dd>

### -field <a id="DO_DEVICE_INITIALIZING"></a><a id="do_device_initializing"></a>DO_DEVICE_INITIALIZING

<dd>
<p>The I/O manager sets this flag when it creates the device object. A device function driver or filter driver clears the flag in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine, after it does the following:</p>
<ul>
<li>Attaches the device object to the device stack.</li>
<li>Establishes the device power state.</li>
<li>Performs a bitwise OR operation on the member with one of the power flags (if it is necessary).</li>
</ul>
<p>The Plug and Play (PnP) manager checks that the flag is clear after the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine returns.</p>
</dd>

### -field <a id="DO_EXCLUSIVE"></a><a id="do_exclusive"></a>DO_EXCLUSIVE

<dd>
<p>Indicates that the driver services an exclusive device, such as a video, serial, parallel, or sound device. WDM drivers must not set this flag. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563827">Specifying Exclusive Access to Device Objects</a> topic.</p>
</dd>

### -field <a id="DO_MAP_IO_BUFFER"></a><a id="do_map_io_buffer"></a>DO_MAP_IO_BUFFER

<dd>
<p>This flag is no longer used. Drivers should not set this flag.</p>
</dd>

### -field <a id="DO_POWER_INRUSH"></a><a id="do_power_inrush"></a>DO_POWER_INRUSH

<dd>
<p>Drivers of devices that require inrush current when the device is turned on must set this flag. A driver cannot set both this flag and DO_POWER_PAGABLE.</p>
</dd>

### -field <a id="DO_POWER_PAGABLE"></a><a id="do_power_pagable"></a>DO_POWER_PAGABLE

<dd>
<p>Pageable drivers that are compatible with Microsoft Windows 2000 and later versions of Windows, are not part of the paging path, and do not require inrush current must set this flag. The system calls such drivers at IRQL = PASSIVE_LEVEL. Drivers cannot set both this flag and DO_POWER_INRUSH. All drivers for WDM, Microsoft Windows 98, and Windows Millennium Edition must set DO_POWER_PAGABLE.</p>
</dd>

### -field <a id="DO_SHUTDOWN_REGISTERED"></a><a id="do_shutdown_registered"></a>DO_SHUTDOWN_REGISTERED

<dd>
<p>Used by the I/O manager to indicate that a driver has registered the device object for shutdown notifications. This flag should not be used by drivers.</p>
</dd>

### -field <a id="DO_VERIFY_VOLUME"></a><a id="do_verify_volume"></a>DO_VERIFY_VOLUME

<dd>
<p>Removable-media drivers set this flag while they process transfer requests. Such drivers should also check for this flag in the target for a transfer request before they transfer any data. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563916">Supporting Removable Media</a> topic.</p>
</dd>
</dl>
<p>For more information about how to set the <b>Flags</b> member, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547807">Initializing a Device Object</a>.</p>
</dd>

### -field <b>Characteristics</b>

<dd>
<p>Specifies one or more system-defined constants, combined with a bitwise OR operation, that provide additional information about the driver's device. These constants include the following:</p>
<p></p>
<dl>

### -field <a id="FILE_AUTOGENERATED_DEVICE_NAME"></a><a id="file_autogenerated_device_name"></a>FILE_AUTOGENERATED_DEVICE_NAME

<dd>
<p>Directs the I/O manager to generate a name for the device, instead of the caller specifying a <i>DeviceName</i> when it calls this routine. The I/O manager makes sure that the name is unique. This characteristic is typically specified by a PnP bus driver to generate a name for a physical device object (PDO) for a child device on the same bus. This characteristic is new starting with Microsoft Windows 2000 and Microsoft Windows 98.</p>
</dd>

### -field <a id="FILE_CHARACTERISTIC_PNP_DEVICE_"></a><a id="file_characteristic_pnp_device_"></a>FILE_CHARACTERISTIC_PNP_DEVICE 

<dd>
<p>Indicates that the device object is part of a Plug and Play (PnP) stack. This characteristic is required if a bus driver (or bus filter driver) registers WMI support for a device object that has not yet received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> request. FILE_CHARACTERISTIC_PNP_DEVICE is also required if a function or filter driver registers for WMI <u>before</u> attaching to its device stack.</p>
</dd>

### -field <a id="FILE_CHARACTERISTIC_TS_DEVICE"></a><a id="file_characteristic_ts_device"></a>FILE_CHARACTERISTIC_TS_DEVICE

<dd>
<p>Indicates that the device object is part of a Terminal Services device stack. Drivers should not set this characteristic.</p>
</dd>

### -field <a id="FILE_CHARACTERISTIC_WEBDAV_DEVICE"></a><a id="file_characteristic_webdav_device"></a>FILE_CHARACTERISTIC_WEBDAV_DEVICE

<dd>
<p>Indicates that a Web-based Distributed Authoring and Versioning (WebDAV) file system is mounted on the device. Drivers should not set this characteristic.</p>
</dd>

### -field <a id="FILE_DEVICE_IS_MOUNTED_"></a><a id="file_device_is_mounted_"></a>FILE_DEVICE_IS_MOUNTED 

<dd>
<p>Indicates that a file system is mounted on the device. Drivers should not set this characteristic.</p>
</dd>

### -field <a id="FILE_DEVICE_SECURE_OPEN"></a><a id="file_device_secure_open"></a>FILE_DEVICE_SECURE_OPEN

<dd>
<p>Directs the I/O manager to apply the security descriptor of the device object to relative opens and trailing file name opens for the device. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542068">Controlling Device Namespace Access</a> topic.</p>
</dd>

### -field <a id="FILE_FLOPPY_DISKETTE"></a><a id="file_floppy_diskette"></a>FILE_FLOPPY_DISKETTE

<dd>
<p>Indicates that the device is a floppy disk device.</p>
</dd>

### -field <a id="FILE_READ_ONLY_DEVICE"></a><a id="file_read_only_device"></a>FILE_READ_ONLY_DEVICE

<dd>
<p>Indicates that the device cannot be written to.</p>
</dd>

### -field <a id="FILE_REMOTE_DEVICE"></a><a id="file_remote_device"></a>FILE_REMOTE_DEVICE

<dd>
<p>Indicates that the device is remote.</p>
</dd>

### -field <a id="FILE_REMOVABLE_MEDIA"></a><a id="file_removable_media"></a>FILE_REMOVABLE_MEDIA

<dd>
<p>Indicates that the storage device supports removable media. Notice that this characteristic indicates removable <i>media</i>, not a removable <i>device</i>. For example, drivers for JAZ drive devices should specify this characteristic, but drivers for PCMCIA flash disks should not.</p>
</dd>

### -field <a id="FILE_VIRTUAL_VOLUME"></a><a id="file_virtual_volume"></a>FILE_VIRTUAL_VOLUME

<dd>
<p>Indicates that the volume is virtual. Drivers should not set this characteristic.</p>
</dd>

### -field <a id="FILE_WRITE_ONCE_MEDIA"></a><a id="file_write_once_media"></a>FILE_WRITE_ONCE_MEDIA

<dd>
<p>Indicates that the device supports write-once media. Drivers do not set this member directly. For more information about how to set device characteristics, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563818">Specifying Device Characteristics</a> topic.</p>
</dd>

### -field <a id="FILE_CHARACTERISTIC_CSV"></a><a id="file_characteristic_csv"></a>FILE_CHARACTERISTIC_CSV

<dd>
<p>Indicates that the device is a Cluster Shared Volume (CSV).</p>
</dd>

### -field <a id="FILE_DEVICE_ALLOW_APPCONTAINER_TRAVERSAL"></a><a id="file_device_allow_appcontainer_traversal"></a>FILE_DEVICE_ALLOW_APPCONTAINER_TRAVERSAL

<dd>
<p>The IO Manager normally performs a full security check for traverse access on every file open when the client is an app container.  Setting of this flag bypasses this enforced traverse access check if the client token already has traverse privileges.</p>
</dd>

### -field <a id="FILE_PORTABLE_DEVICE"></a><a id="file_portable_device"></a>FILE_PORTABLE_DEVICE

<dd>
<p>Indicates that the underlying stack considers the device portable. This is used by the storage stack and means that the device is not in the local machine container and is not on a fixed bus type.</p>
</dd>
</dl>
</dd>

### -field <b>Vpb</b>

<dd>
<p>A pointer to the volume parameter block (VPB) that is associated with the device object. For file system drivers, the VPB can provide a connection to any unnamed logical device object that represents an instance of a mounted volume. This is an opaque member.</p>
</dd>

### -field <b>DeviceExtension</b>

<dd>
<p>A pointer to the device extension. The structure and contents of the device extension are driver-defined. The size is driver-determined, specified in the driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407">IoCreateDeviceSecure</a>. For more information about device extensions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543119">Device Extensions</a>. This is a read-only member. However, the object that the member points to can be modified by the driver.</p>
</dd>

### -field <b>DeviceType</b>

<dd>
<p>Set by <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407">IoCreateDeviceSecure</a> by using the value that is specified for that routine's <i>DeviceType</i> parameter. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563821">Specifying Device Types</a> topic.</p>
</dd>

### -field <b>StackSize</b>

<dd>
<p>Specifies the minimum number of stack locations in IRPs to be sent to this driver. <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407">IoCreateDeviceSecure</a> set this member to 1 in newly created device objects; lowest-level drivers can therefore ignore this member. The I/O manager automatically sets the <b>StackSize</b> member in a higher-level driver's device object to the appropriate value if the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548294">IoAttachDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548300">IoAttachDeviceToDeviceStack</a>. Only a higher-level driver that chains itself over another driver with <b>IoGetDeviceObjectPointer</b> must explicitly set the value of <b>StackSize</b> in its own device object(s) to 1 + the <b>StackSize</b> value of the next-lower driver's device object.</p>
</dd>

### -field <b>Queue</b>

<dd>
<p>Used internally by the I/O manager to queue the device object when it is required. This is an opaque member.</p>
<dl>

### -field <b>ListEntry</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554296">LIST_ENTRY</a> structure that contains forward and backward pointers for a doubly linked list.</p>
</dd>

### -field <b>Wcb</b>

<dd>
<p>Device context information used by I/O manager.</p>
</dd>
</dl>
</dd>

### -field <b>AlignmentRequirement</b>

<dd>
<p>Specifies the device's address alignment requirement for data transfers. The value must be one of the FILE_<i>XXX</i>_ALIGNMENT values that are defined in Wdm.h. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547807">Initializing a Device Object</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546530">GetDmaAlignment</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a> topics.</p>
</dd>

### -field <b>DeviceQueue</b>

<dd>
<p>The device queue object for the device object. The device queue object contains any IRPs that are waiting to be processed by the driver that is associated with the device object. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544156">Driver-Managed IRP Queues</a> topic. This is an opaque member.</p>
</dd>

### -field <b>Dpc</b>

<dd>
<p>The deferred procedure call (DPC) object for the device object. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548024">Introduction to DPC Objects</a> topic. This is an opaque member.</p>
</dd>

### -field <b>ActiveThreadCount</b>

<dd>
<p>Reserved for future use. This is an opaque member.</p>
</dd>

### -field <b>SecurityDescriptor</b>

<dd>
<p>Specifies a security descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>) for the device object when the device object is created. If this member is <b>NULL</b>, the device object receives default security settings. This is a read-only member, although the member can be modified through the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567106">ZwSetSecurityObject</a>function.</p>
</dd>

### -field <b>DeviceLock</b>

<dd>
<p>A synchronization event object that is allocated by the I/O manager. The I/O manager obtains his event object before it dispatches a mount or mount-verify request to a file-system driver. This is an opaque member.</p>
</dd>

### -field <b>SectorSize</b>

<dd>
<p>If the device object does not represent a volume, this member is set to zero. If the device object represents a volume, this member specifies the volume's sector size, in bytes. The I/O manager uses this member to make sure that all read operations, write operations, and set file position operations that are issued are aligned correctly when intermediate buffering is disabled. A default system bytes-per-sector value is used when the device object is created, however, file system drivers; and more rarely, legacy and minifilter drivers, can update this value that is based on the geometry of the underlying volume hardware when a mount occurs. Other drivers should not modify this member.</p>
</dd>

### -field <b>Spare1</b>

<dd>
<p>Reserved for system use. This is an opaque member.</p>
</dd>

### -field <b>DeviceObjectExtension</b>

<dd>
<p>A pointer to a device object extension that is used by the I/O manager and PnP manager to store information about the state of the device. This is an opaque member.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. This is an opaque member.</p>
</dd>
</dl>

## -remarks
<p>The operating system represents devices by device objects. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543153">Device Objects and Device Stacks</a> topic.</p>

<p>Drivers create device objects by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407">IoCreateDeviceSecure</a> routines. For more information about how to create device objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542862">Creating a Device Object</a>.</p>

<p>A device object is partially opaque. Drivers do not set members of the device object directly, unless otherwise documented. For more information about the members that drivers can modify directly, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547807">Initializing a Device Object</a>. For information about other device object properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559925">Properties of Device Objects</a>.</p>

<p>Opaque members within a device object must be considered inaccessible. Drivers that have dependencies on object member locations or access to opaque members might not remain portable and interoperable with other drivers over time.</p>

<p>The system-supplied video port driver sets up the fields of the device objects that it creates on behalf of <a href="https://msdn.microsoft.com/3a540bfe-f340-4f12-acee-323b97683074">video miniport drivers</a>.</p>

<p>The system-supplied SCSI port driver sets up the fields of the device objects that it creates on behalf of <a href="NULL">SCSI miniport drivers</a>.</p>

<p>The system-supplied NDIS library sets up the fields of the device objects that it creates on behalf of <a href="NULL">NDIS miniport drivers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548294">IoAttachDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548300">IoAttachDeviceToDeviceStack</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549083">IoDeleteDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549198">IoGetDeviceObjectPointer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DEVICE_OBJECT structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
