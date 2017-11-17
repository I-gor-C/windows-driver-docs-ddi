# Declarations in the strmini header
This header Strmini contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PHW_TIMER_ROUTINE callback function](nc-strmini-phw-timer-routine.md) | TBD |
| [PHW_REQUEST_TIMEOUT_HANDLER callback function](nc-strmini-phw-request-timeout-handler.md) | TBD |
| [PHW_INTERRUPT callback function](nc-strmini-phw-interrupt.md) | TBD |
| [PHW_CANCEL_SRB callback function](nc-strmini-phw-cancel-srb.md) | TBD |
| [PHW_RECEIVE_DEVICE_SRB callback function](nc-strmini-phw-receive-device-srb.md) | TBD |
| [PHW_RECEIVE_STREAM_CONTROL_SRB callback function](nc-strmini-phw-receive-stream-control-srb.md) | TBD |
| [PHW_CLOCK_FUNCTION callback function](nc-strmini-phw-clock-function.md) | TBD |
| [PHW_RESET_ADAPTER callback function](nc-strmini-phw-reset-adapter.md) | TBD |
| [PHW_QUERY_CLOCK_ROUTINE callback function](nc-strmini-phw-query-clock-routine.md) | TBD |
| [PHW_RECEIVE_STREAM_DATA_SRB callback function](nc-strmini-phw-receive-stream-data-srb.md) | TBD |
| [PHW_PRIORITY_ROUTINE callback function](nc-strmini-phw-priority-routine.md) | TBD |
| [PHW_EVENT_ROUTINE callback function](nc-strmini-phw-event-routine.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [STREAM_PRIORITY enumeration](ne-strmini--stream-priority.md) | TBD. |
| [STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE enumeration](ne-strmini--stream-minidriver-device-notification-type.md) | TBD. |
| [STREAM_DEBUG_LEVEL enumeration](ne-strmini-stream-debug-level.md) | The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output. |
| [TIME_FUNCTION enumeration](ne-strmini-time-function.md) | TBD. |
| [SRB_COMMAND enumeration](ne-strmini--srb-command.md) | TBD. |
| [STREAM_BUFFER_TYPE enumeration](ne-strmini-stream-buffer-type.md) | This enumeration defines the buffer types for StreamClassGetPhysicalAddress. |
| [STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration](ne-strmini--stream-minidriver-stream-notification-type.md) | TBD. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [StreamClassDeviceNotification function](nf-strmini-streamclassdevicenotification.md) | Minidrivers use the StreamClassDeviceNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [StreamClassFilterReenumerateStreams function](nf-strmini-streamclassfilterreenumeratestreams.md) | TBD |
| [StreamClassReenumerateStreams function](nf-strmini-streamclassreenumeratestreams.md) | TBD |
| [StreamClassRegisterAdapter function](nf-strmini-streamclassregisteradapter.md) | TBD |
| [StreamClassGetNextEvent function](nf-strmini-streamclassgetnextevent.md) | Minidrivers can use the StreamClassGetNextEvent routine to search the event queue of a device or of a particular stream. |
| [StreamClassReadWriteConfig function](nf-strmini-streamclassreadwriteconfig.md) | The StreamClassReadWriteConfig routine reads or writes configuration data for the minidriver's parent bus driver. |
| [StreamClassGetDmaBuffer function](nf-strmini-streamclassgetdmabuffer.md) | The StreamClassGetDmaBuffer routine returns a pointer to the DMA buffer that the class driver allocates for the minidriver. |
| [StreamClassDebugPrint function](nf-strmini-streamclassdebugprint.md) | In a checked build environment, the minidriver can use the StreamClassDebugPrint routine to print debug messages to the application window and to the Debugger Command window. |
| [StreamClassScheduleTimer function](nf-strmini-streamclassscheduletimer.md) | The minidriver calls the StreamClassScheduleTimer routine to schedule a timer, and to specify a routine that is called when the timer expires. |
| [StreamClassGetPhysicalAddress function](nf-strmini-streamclassgetphysicaladdress.md) | The StreamClassGetPhysicalAddress routine translates a virtual memory address to a physical memory address and locks the corresponding physical memory for a DMA operation. |
| [StreamClassDebugAssert function](nf-strmini-streamclassdebugassert.md) | A minidriver can use the StreamClassDebugAssert routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger. |
| [StreamClassCompleteRequestAndMarkQueueReady function](nf-strmini-streamclasscompleterequestandmarkqueueready.md) | The StreamClassCompleteRequestAndMarkQueueReady routine completes a request, and signals the class driver that the minidriver is ready to receive a new request of the same type. |
| [DebugPrint function](nf-strmini-debugprint.md) | TBD |
| [StreamClassStreamNotification function](nf-strmini-streamclassstreamnotification.md) | Streams use the StreamClassStreamNotification routine to notify the class driver that it has completed a stream request, or that an event has occurred. |
| [DEBUG_ASSERT function](nf-strmini-debug-assert.md) | TBD |
| [StreamClassCallAtNewPriority function](nf-strmini-streamclasscallatnewpriority.md) | The StreamClassCallAtNewPriority routine schedules a routine to be called at a different priority. |
| [StreamClassQueryMasterClockSync function](nf-strmini-streamclassquerymasterclocksync.md) | The minidriver may call the StreamClassQueryMasterClockSync routine to synchronously query a stream's master clock. |
| [StreamClassRegisterFilterWithNoKSPins function](nf-strmini-streamclassregisterfilterwithnokspins.md) | The StreamClassRegisterFilterWithNoKSPins routine is used to register filter drivers with Microsoft DirectShow that have no kernel streaming pins and, therefore, do not stream in kernel mode. |
| [StreamClassQueryMasterClock function](nf-strmini-streamclassquerymasterclock.md) | When the minidriver calls the StreamClassQueryMasterClock routine, the class driver queries the appropriate time value of the master clock asynchronously, and passes the result to the routine passed in the ClockCallbackRoutine parameter. |
| [StreamClassAbortOutstandingRequests function](nf-strmini-streamclassabortoutstandingrequests.md) | The StreamClassAbortOutstandingRequests routine aborts all outstanding requests, either to a particular stream, or to the entire driver. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [STREAM_TIME_REFERENCE structure](ns-strmini--stream-time-reference.md) | TBD. |
| [PORT_CONFIGURATION_INFORMATION structure](ns-strmini--port-configuration-information~r1.md) | PORT_CONFIGURATION_INFORMATION describes the hardware settings of a streaming minidriver's device. The class driver fills in most members with information provided by the operating system. |
| [HW_STREAM_REQUEST_BLOCK structure](ns-strmini--hw-stream-request-block.md) | The stream class driver uses the HW_STREAM_REQUEST_BLOCK structure to pass information to and from the minidriver, using minidriver provided callbacks. |
| [HW_CLOCK_OBJECT structure](ns-strmini--hw-clock-object.md) | The HW_CLOCK_OBJECT structure describes the clock associated with a stream. |
| [PKSSCATTER_GATHER structure](ns-strmini-pksscatter-gather.md) | TBD. |
| [STREAM_PROPERTY_DESCRIPTOR structure](ns-strmini--stream-property-descriptor.md) | STREAM_PROPERTY_DESCRIPTOR specifies the parameters of property get/set requests that the class driver passes to the minidriver. |
| [HW_STREAM_INFORMATION structure](ns-strmini--hw-stream-information.md) | The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an HW_STREAM_DESCRIPTOR structure. |
| [HW_STREAM_OBJECT structure](ns-strmini--hw-stream-object~r1.md) | HW_STREAM_OBJECT describes an instance of a minidriver stream. |
| [HW_STREAM_DESCRIPTOR structure](ns-strmini--hw-stream-descriptor.md) | The minidriver uses the HW_STREAM_DESCRIPTOR structure to return stream information to the stream class driver. |
| [STREAM_DATA_INTERSECT_INFO structure](ns-strmini--stream-data-intersect-info.md) | STREAM_DATA_INTERSECT_INFO describes the parameters of a data intersection operation. |
| [HW_TIME_CONTEXT structure](ns-strmini--hw-time-context.md) | The class driver passes an HW_TIME_CONTEXT structure as a parameter to be filled in by a stream's StrMiniClock routine, or returns a completed HW_TIME_CONTEXT structure when it responds to a StreamClassQueryMasterClock or StreamClassQueryMasterClockSync request. |
| [HW_EVENT_DESCRIPTOR structure](ns-strmini--hw-event-descriptor.md) | When the class driver calls one of the minidriver's StrMiniEvent routines, it passes a pointer to an HW_EVENT_DESCRIPTOR structure to describe the event as enabled or disabled. |
| [HW_INITIALIZATION_DATA structure](ns-strmini--hw-initialization-data.md) | The HW_INITIALIZATION_DATA structure specifies the basic information the class driver needs to begin initializing the minidriver. |
| [STREAM_METHOD_DESCRIPTOR structure](ns-strmini--stream-method-descriptor.md) | TBD. |
| [ACCESS_RANGE structure](ns-strmini--access-range.md) | TBD |
| [HW_STREAM_HEADER structure](ns-strmini--hw-stream-header.md) | The HW_STREAM_HEADER structure describes the kernel streaming semantics supported by the minidriver as a whole, as part of a HW_STREAM_DESCRIPTOR structure. |

This header is used in these topics:

- [stream](..content/_stream)
